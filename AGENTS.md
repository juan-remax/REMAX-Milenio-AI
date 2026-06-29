# REMAX Milenio AI — AGENTS.md

## Reglas persistentes del proyecto

### 1. Spec-Driven Development
No se escribe código sin una spec aprobada previamente. Toda implementación debe estar documentada en `specs/features/<feature>/spec.md`.

### 2. Confirmación humana
Toda acción crítica requiere confirmación explícita del usuario antes de ejecutarse. Se considera acción crítica:
- Enviar mensajes a clientes reales
- Crear o modificar issues en GitHub
- Modificar datos de clientes o propiedades
- Publicar contenido en portales o redes sociales

### 3. Trazabilidad
Cada tarea se registra en GitHub Issues con estado y decisión. Las conversaciones importantes se loguean en base de datos.

### 4. Stack fijo
Python 3.11+ / FastAPI / aiogram 3.x / PostgreSQL 16 / SQLAlchemy 2.0.
No cambiar sin decisión documentada en `specs/constitution/tech-stack.md`.

### 5. Pruebas obligatorias
Toda feature nueva debe tener tests unitarios. Las PR sin tests no se aceptan.

### 6. Logging
Toda interacción del bot se registra en la tabla `conversations` para trazabilidad y memoria operativa.

### 7. Seguridad
- `.env` nunca se commitea (está en `.gitignore`)
- Las variables de entorno se usan para todos los secretos
- Solo usuarios autorizados (whitelist por Telegram user_id) pueden usar el bot

### 8. Metodología de trabajo
- **Plan Mode**: Primero se presenta el plan, se espera aprobación, luego se implementa
- **Commits**: Mensajes descriptivos en español o inglés
- **Documentación**: Toda decisión técnica se documenta en `docs/decisions.md`
