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

## Inicio rápido

```bash
cp .env.example .env
# Editar .env con tu token de Telegram y GitHub
docker compose up -d
```

## Features

| # | Feature | Estado |
|---|---------|--------|
| 1 | Telegram Bot (comandos, auth, mensajes) | 📋 Planificado |
| 2 | Agent Router (clasificador de intención) | 📋 Planificado |
| 3 | Agente de Leads | 📋 Planificado |
| 4 | Agente de Propiedades | 📋 Planificado |
| 5 | Agente de Marketing | 📋 Planificado |
| 6 | GitHub Issues Bridge | 📋 Planificado |
| 7 | Memoria operativa (logs) | 📋 Planificado |

## Documentación

- [Arquitectura](docs/architecture.md)
- [Specs constitucionales](specs/constitution/mission.md)
- [Features](specs/features/)

## Licencia

Proyecto privado — REMAX Milenio
