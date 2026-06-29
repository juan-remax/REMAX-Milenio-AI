# Seguridad — REMAX Milenio AI

## Perímetro

- **Autenticación**: Solo usuarios Telegram autorizados (whitelist por `user_id` en `.env`) pueden interactuar con el bot.
- **Token**: El token del bot de Telegram y el token de GitHub se almacenan exclusivamente en `.env`, nunca en el repositorio.
- **Base de datos**: PostgreSQL corre en red interna de Docker, no expuesta al exterior.
- **Firewall**: No se abren puertos innecesarios. Solo se expone el webhook del bot si es necesario.

## Datos

- **Consentimiento**: No se almacenan datos sensibles de clientes sin consentimiento explícito del operador.
- **PII**: Los logs no contienen información personal identificable (PII) a menos que sea estrictamente necesario para la operación.
- **Retención**: Los mensajes de Telegram se almacenan solo para trazabilidad operativa. Se define política de retención máxima de 12 meses.
- **Cifrado**: La conexión a PostgreSQL usa cifrado si está disponible. Las contraseñas se almacenan hasheadas.

## GitHub

- **Token mínimo**: El token de GitHub tiene permisos exclusivos para issues y comentarios en el repositorio específico.
- **Sin push directo**: No se permite push a ramas protegidas sin revisión humana.
- **Workflows**: Los GitHub Actions usan solo los permisos necesarios para su ejecución.

## Confirmaciones humanas

- **Acciones críticas**: Toda acción que afecte a un cliente real (enviar mensaje, modificar datos, publicar) requiere confirmación explícita del operador.
- **Doble confirmación**: Las acciones especialmente sensibles (enviar email, publicar en portales) requieren doble confirmación: "¿Estás seguro?" + "Confirma escribiendo SÍ".
- **Timeouts**: Si el operador no confirma en 5 minutos, la acción se cancela automáticamente.

## Plan de respuesta a incidentes

1. Si se detecta acceso no autorizado, revocar tokens inmediatamente.
2. Si hay fuga de datos, notificar al operador y rotar todas las credenciales.
3. Auditoría mensual de logs de acceso.
