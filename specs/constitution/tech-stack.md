# Stack Tecnológico — REMAX Milenio AI

## Stack aprobado

| Componente | Tecnología | Versión | Razón |
|---|---|---|---|
| Backend | Python + FastAPI | 3.11+ / 0.111+ | Async nativo, tipado estático, ecosistema maduro para IA/agentes |
| Bot Telegram | aiogram | 3.x | Librería Python async más madura para bots Telegram |
| Base de datos | PostgreSQL | 16 | Relacional, robusto, preparado para pgvector futuro |
| ORM | SQLAlchemy + Alembic | 2.0 | Estándar Python, migrations maduras, async support |
| GitHub API | PyGithub | 2.x | Integración nativa con issues y repos |
| Testing | pytest + pytest-asyncio | 8.x | Estándar Python, soporte async |
| Linting | ruff | 0.x | Extremadamente rápido, reemplaza flake8/isort/black |
| Infraestructura | Docker + docker-compose | 24+ / 3.8+ | Entorno reproducible |
| Task runner | Makefile | — | Comandos comunes estandarizados |
| Logging | loguru | 0.7+ | Logging simple y potente |

## Stack explícitamente descartado

| Tecnología | Razón del descarte |
|---|---|
| Node.js / NestJS | El ecosistema Python para agentes/IA está más maduro (LangChain, LlamaIndex). Velocidad de prototipado mayor con Python para MVP. |
| MongoDB | PostgreSQL es más versátil para datos relacionales del dominio inmobiliario. pgvector en el futuro para búsqueda semántica. |
| Redis | Innecesario para MVP. Se puede añadir como caché en fases posteriores si hay necesidad de rendimiento. |
| Telegraf (Node.js) | aiogram ofrece mejor DX para Python y estamos comprometidos con Python como stack principal. |

## Criterios de decisión

1. **Velocidad de prototipado** — Poder tener MVP funcional en días, no semanas.
2. **Ecosistema IA** — El stack debe permitir incorporar agentes inteligentes sin fricción.
3. **Madurez** — Tecnologías probadas con comunidad activa.
4. **Portabilidad** — Docker como requisito no negociable.
5. **Costo** — Stack 100% open source sin costos de licencia.
