# Feature 002 — Integración Inmovilla CRM

## Descripción

Conexión bidireccional entre REMAX Milenio AI y el CRM Inmovilla mediante su API REST v1.
Los leads creados por el bot se sincronizan automáticamente como clientes en Inmovilla.
Las propiedades de Inmovilla se pueden consultar e importar localmente.

## Endpoints de Inmovilla utilizados

| Método | Endpoint | Uso |
|---|---|---|
| GET | `/clientes/?cod_cli={cod_cli}` | Obtener cliente por ID |
| POST | `/clientes/` | Crear cliente desde lead |
| PUT | `/clientes/` | Actualizar cliente |
| GET | `/clientes/buscar/?telefono=&email=` | Buscar cliente por teléfono/email |
| GET | `/propiedades/?cod_ofer={cod_ofer}` | Obtener propiedad por ID |
| GET | `/propiedades/?listar` | Listar propiedades |
| GET | `/enums/?tipos` | Obtener tipos de propiedad |
| GET | `/enums/?ciudades` | Obtener catálogo de ciudades |

## Autenticación

- Token API Rest proporcionado por Inmovilla (se configura en settings)
- Se envía en header `Token` en todas las peticiones
- Formato: JSON con `Content-Type: application/json`

## Flujos

### 1. Lead → Cliente en Inmovilla
1. Usuario crea lead vía bot
2. El agente lead_agent llama a `inmovilla_client.create_client()`
3. Se guarda `cod_cli` de Inmovilla en el lead local
4. Si falla, se loguea error y el lead queda pendiente de sincronización

### 2. Buscar cliente en Inmovilla
1. Usuario escribe "buscar cliente Juan Pérez" o usa comando `/buscarcliente`
2. Bot consulta `GET /clientes/buscar/` con teléfono o nombre
3. Muestra resultados en formato legible

### 3. Sincronizar propiedades
1. Usuario usa `/sincronizar` para traer propiedades desde Inmovilla
2. Bot consulta `GET /propiedades/?listar` con paginación
3. Las propiedades se almacenan en la tabla `properties` local
4. Se evitan duplicados por `cod_ofer`

## Rate Limiting

- Enums: máx 2 peticiones/minuto
- Clientes/Propiedades: máx 20 peticiones/minuto
- El cliente HTTP implementa espera automática si recibe HTTP 408

## Configuración

Variables de entorno nuevas:
- `INMOVILLA_TOKEN` — Token API Rest
- `INMOVILLA_NUMAGENCIA` — Número de agencia en Inmovilla

## Modelos de datos

Se extiende el modelo `Lead` con campo `inmovilla_cod_cli: str | None`.
No se requieren nuevos modelos (properties ya existe).

## Criterios de aceptación

- [ ] Crear cliente en Inmovilla al crear lead (si hay token configurado)
- [ ] Buscar clientes en Inmovilla por teléfono o email
- [ ] Sincronizar propiedades desde Inmovilla bajo demanda
- [ ] Rate limiting manejado gracefulmente
- [ ] Fallo en Inmovilla no bloquea al bot (falla silenciosa + log)
