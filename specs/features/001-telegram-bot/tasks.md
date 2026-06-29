# Tareas — Feature 001

Cada tarea se corresponde con un issue de GitHub.

## Tarea 001.1 — Configurar proyecto

**Issue**: `[FEAT-001.1] Inicializar proyecto Python + FastAPI`

**Checklist**:
- [ ] Crear `pyproject.toml` con dependencias
- [ ] Configurar `src/main.py` como entry point de FastAPI
- [ ] Configurar `src/config/settings.py` con Pydantic Settings
- [ ] Verificar que la app arranca correctamente

**Criterios de aceptación**:
- `uvicorn src.main:app --reload` funciona sin errores
- `GET /health` devuelve `{"status": "ok"}`

**Dependencias**: Ninguna

---

## Tarea 001.2 — Handlers básicos

**Issue**: `[FEAT-001.2] Implementar handlers /start y /help`

**Checklist**:
- [ ] Configurar aiogram dispatcher
- [ ] Implementar handler `/start` con mensaje de bienvenida
- [ ] Implementar handler `/help` con lista de comandos

**Criterios de aceptación**:
- `/start` responde con nombre del bot y bienvenida
- `/help` lista todos los comandos disponibles

**Dependencias**: 001.1

---

## Tarea 001.3 — Middleware de autenticación

**Issue**: `[FEAT-001.3] Implementar autenticación por whitelist`

**Checklist**:
- [ ] Crear middleware que intercepta todos los mensajes
- [ ] Validar `user_id` contra `ALLOWED_USER_IDS`
- [ ] Responder con error si no autorizado

**Criterios de aceptación**:
- Usuarios en whitelist pueden usar el bot
- Usuarios fuera de whitelist reciben mensaje de rechazo
- Los handlers no se ejecutan para usuarios no autorizados

**Dependencias**: 001.2

---

## Tarea 001.4 — Base de datos

**Issue**: `[FEAT-001.4] Configurar PostgreSQL + SQLAlchemy + modelos`

**Checklist**:
- [ ] Configurar engine asíncrono SQLAlchemy
- [ ] Crear modelo `Conversation` (id, user_id, message, response, timestamp)
- [ ] Crear modelo `Lead` (campos básicos: nombre, telefono, email, estado)
- [ ] Configurar Alembic para migrations
- [ ] Crear migration inicial

**Criterios de aceptación**:
- `alembic upgrade head` crea las tablas correctamente
- Se puede insertar y consultar desde Python

**Dependencias**: 001.1

---

## Tarea 001.5 — Router de mensajes

**Issue**: `[FEAT-001.5] Implementar Agent Router básico`

**Checklist**:
- [ ] Crear `src/agents/router.py` con clasificador por regex/keywords
- [ ] Implementar intenciones iniciales: lead, propiedad, marketing, tarea, ayuda
- [ ] Conectar handler de mensaje libre con el router
- [ ] Delegar a agente correspondiente o responder "no entendí"

**Criterios de aceptación**:
- "nuevo cliente" → clasifica como intención `lead`
- "quiero publicar" → clasifica como intención `marketing`
- Mensaje irreconocible → respuesta amigable pidiendo reformular

**Dependencias**: 001.2, 001.4

---

## Tarea 001.6 — Docker

**Issue**: `[FEAT-001.6] Dockerizar la aplicación`

**Checklist**:
- [ ] Crear `Dockerfile` multi-etapa
- [ ] Crear `docker-compose.yml` con app + postgres
- [ ] Verificar que `docker compose up` funciona

**Criterios de aceptación**:
- `docker compose up` levanta app + db
- El bot responde desde el contenedor

**Dependencias**: 001.5
