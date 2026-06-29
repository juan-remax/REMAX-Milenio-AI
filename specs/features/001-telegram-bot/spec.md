# Feature 001 — Telegram Bot

## Descripción

Bot de Telegram que funciona como interfaz principal del sistema REMAX Milenio AI.
Recibe mensajes del usuario, los clasifica por intención y los enruta al agente especializado correspondiente.

## Comandos

| Comando | Descripción | Auth |
|---|---|---|
| `/start` | Mensaje de bienvenida e instrucciones | Sí |
| `/help` | Lista de comandos disponibles | Sí |
| `/nuevolead` | Inicia flujo de alta de lead | Sí |
| `/nuevapropiedad` | Inicia flujo de alta de propiedad | Sí |
| `/tareas` | Lista tareas pendientes | Sí |
| `/estado` | Resumen del día | Sí |
| `/cancelar` | Cancela la conversación actual | Sí |

## Flujo de mensaje libre

1. Usuario envía un mensaje de texto
2. El handler recibe el mensaje
3. El middleware de autenticación verifica que el user_id está en whitelist
4. El Agent Router clasifica la intención (regex + keywords)
5. Se delega al agente correspondiente
6. El agente procesa y responde
7. La conversación se loguea en DB

## Autenticación

- Middleware que intercepta todos los mensajes
- Compara `message.from_user.id` contra `ALLOWED_USER_IDS` del `.env`
- Si no está autorizado, responde con mensaje genérico y no procesa

## Respuestas

- Formato Markdown con emojis
- Mensajes informativos, confirmaciones y errores claros
- Tiempo máximo de respuesta: 30 segundos

## Criterios de aceptación

- [ ] El bot responde a `/start` y `/help`
- [ ] Los usuarios no autorizados reciben mensaje de rechazo
- [ ] Los mensajes de texto libre se clasifican por intención
- [ ] Las conversaciones se registran en la base de datos
- [ ] El bot maneja timeouts y errores gracefulmente
