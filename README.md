# REMAX Milenio AI

Asistente inmobiliario inteligente para la oficina **REMAX Milenio**.

Conecta **Telegram**, **OpenCode** y **GitHub** para automatizar la gestión diaria de leads, propiedades, marketing y tareas operativas de una actividad inmobiliaria real.

## Stack

| Componente | Tecnología |
|---|---|
| Backend | Python 3.11+ / FastAPI |
| Bot Telegram | aiogram 3.x |
| Base de datos | PostgreSQL 16 + SQLAlchemy 2.0 |
| Infraestructura | Docker + docker-compose |
| GitHub | PyGithub + GitHub Actions |

## Requisitos

- Python 3.11+
- PostgreSQL 16 (o Docker)
- Token de Telegram (de [@BotFather](https://t.me/BotFather))
- Token de GitHub (opcional, para issues)

## Inicio rápido

```bash
# 1. Configurar variables de entorno
cp .env.example .env
# Editar .env con tu token y user_id

# 2. Instalar dependencias
pip install -e ".[dev]"

# 3. Iniciar base de datos (requiere Docker)
docker compose up -d db

# 4. Iniciar el bot
uvicorn src.main:app --reload
```

## Features

| # | Feature | Estado |
|---|---------|--------|
| 1 | Telegram Bot (comandos, auth, mensajes) | ✅ Implementado |
| 2 | Agent Router (clasificador de intención) | ✅ Implementado |
| 3 | Agente de Leads | ✅ Implementado |
| 4 | Agente de Propiedades | ✅ Implementado |
| 5 | Agente de Marketing | ✅ Implementado |
| 6 | GitHub Issues Bridge | ✅ Implementado |
| 7 | Memoria operativa (logs) | ✅ Implementado |
| 8 | Confirmación humana (guardrails) | ✅ Implementado |

## Tests

```bash
pytest tests/ -v    # 30 tests
ruff check src/     # 0 errores
```

## Documentación

- [Arquitectura](docs/architecture.md)
- [Specs constitucionales](specs/constitution/mission.md)
- [Features](specs/features/)

## Licencia

Proyecto privado — REMAX Milenio
