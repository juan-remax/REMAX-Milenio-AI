from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy import select

from src.database.models.property import Property
from src.database.session import async_session_factory
from src.services.github_service import github_service
from src.services.inmovilla_client import inmovilla_client

router = Router()


@router.message(Command("nuevolead"))
async def cmd_nuevo_lead(message: Message):
    await message.answer(
        "👤 *Nuevo Lead*\n\n"
        "Dime los datos del lead en este formato:\n\n"
        "`Nombre | Teléfono | Email | Tipo`\n\n"
        "*Tipos:* comprador, vendedor, inversor\n\n"
        "Ejemplo:\n"
        "`Juan Pérez | 612345678 | juan@email.com | comprador`"
    )


@router.message(Command("nuevapropiedad"))
async def cmd_nueva_propiedad(message: Message):
    await message.answer(
        "🏠 *Nueva Propiedad*\n\n"
        "Dime los datos en este formato:\n\n"
        "`Título | Dirección | Tipo | Precio | m² | Hab | Baños`\n\n"
        "*Tipos:* piso, casa, local, terreno\n\n"
        "Ejemplo:\n"
        "`Piso centro | Calle Mayor 10 | piso | 180000 | 90 | 3 | 2`"
    )


@router.message(Command("tareas"))
async def cmd_tareas(message: Message):
    issues = await github_service.list_open_issues()
    if not issues:
        await message.answer("📋 *Tareas*\n\nNo hay tareas pendientes en GitHub.")
        return

    lines = [f"• #{i['number']} - {i['title']}" for i in issues[:10]]
    await message.answer("📋 *Tareas pendientes:*\n\n" + "\n".join(lines))


@router.message(Command("estado"))
async def cmd_estado(message: Message):
    await message.answer(
        "📊 *Resumen del día*\n\n"
        "• Leads nuevos: 0\n"
        "• Propiedades activas: 0\n"
        "• Tareas pendientes: —\n"
        "• Última actividad: —\n\n"
        "_Los datos se mostrarán cuando la base de datos esté conectada._"
    )


@router.message(Command("cancelar"))
async def cmd_cancelar(message: Message):
    await message.answer("✅ Operación cancelada. ¿En qué más puedo ayudarte?")


@router.message(Command("buscarcliente"))
async def cmd_buscar_cliente(message: Message):
    if not inmovilla_client.enabled:
        await message.answer("⚠️ Inmovilla no está configurado. Añade INMOVILLA_TOKEN en .env")
        return

    args = message.text.replace("/buscarcliente", "", 1).strip()
    if not args:
        await message.answer(
            "🔍 *Buscar Cliente en Inmovilla*\n\n"
            "Uso: `/buscarcliente teléfono` o `/buscarcliente email@correo.com`"
        )
        return

    telefono = args if args.isdigit() or args.startswith("+") else ""
    email = args if "@" in args else ""

    results = await inmovilla_client.search_client(telefono=telefono, email=email)
    if not results:
        await message.answer(f"🔍 No se encontraron clientes con: `{args}`")
        return

    lines = ["🔍 *Clientes encontrados en Inmovilla:*\n"]
    for r in results[:5]:
        nombre = f"{r.get('nombre', '')} {r.get('apellidos', '')}".strip()
        lines.append(
            f"• *{nombre}* — #{r.get('cod_cli', '?')}\n"
            f"  📞 {r.get('telefono1', '—')}  ✉️ {r.get('email', '—')}"
        )
    if len(results) > 5:
        lines.append(f"\n_Mostrando 5 de {len(results)} resultados_")

    await message.answer("\n".join(lines))


@router.message(Command("sincronizar"))
async def cmd_sincronizar(message: Message):
    if not inmovilla_client.enabled:
        await message.answer("⚠️ Inmovilla no está configurado. Añade INMOVILLA_TOKEN en .env")
        return

    await message.answer("🔄 Obteniendo listado de propiedades desde Inmovilla...")

    props_list = await inmovilla_client.list_properties()
    if not props_list:
        await message.answer("No se encontraron propiedades en Inmovilla.")
        return

    total = len(props_list)
    await message.answer(f"📋 Se encontraron {total} propiedades. Descargando detalles...")

    imported = 0
    updated = 0
    errors = 0

    for i, item in enumerate(props_list):
        cod_ofer = str(item.get("cod_ofer", ""))
        if not cod_ofer:
            continue

        details = await inmovilla_client.get_property(cod_ofer)
        if not details:
            errors += 1
            continue

        async with async_session_factory() as session:
            result = await session.execute(
                select(Property).where(Property.cod_ofer == cod_ofer)
            )
            existing = result.scalar_one_or_none()

            ref = details.get("ref", cod_ofer)
            title = f"{details.get('nbtipo', 'Propiedad')} - Ref {ref}"
            address = f"{details.get('calle', '')} {details.get('numero', '')}".strip()
            price = float(details.get("precioinmo", 0) or 0)
            sqm = float(details.get("m_cons", 0) or 0) or None
            bedrooms = details.get("total_hab")
            bathrooms = details.get("banyos")

            if existing:
                existing.title = title
                existing.address = address
                existing.price = price
                existing.square_meters = sqm
                existing.bedrooms = bedrooms
                existing.bathrooms = bathrooms
                updated += 1
            else:
                prop = Property(
                    cod_ofer=cod_ofer,
                    title=title,
                    address=address,
                    property_type=details.get("nbtipo", "unknown"),
                    price=price,
                    square_meters=sqm,
                    bedrooms=bedrooms,
                    bathrooms=bathrooms,
                    status="active",
                )
                session.add(prop)
                imported += 1

            await session.commit()

        if (i + 1) % 10 == 0:
            await message.answer(f"⏳ Progreso: {i + 1}/{total}")

    await message.answer(
        f"✅ *Sincronización completa!*\n\n"
        f"• Nuevas: {imported}\n"
        f"• Actualizadas: {updated}\n"
        f"{'• Errores: ' + str(errors) if errors else ''}"
    )
