# Plan de Implementación — Feature 001

## Prioridades

| Prioridad | Tarea | Dependencias |
|---|---|---|
| P0 | Configurar proyecto Python + FastAPI + aiogram | — |
| P0 | Handler `/start` y `/help` | P0 anterior |
| P0 | Middleware de autenticación | P0 anterior |
| P1 | Handler de mensaje libre con router simple | P0 auth |
| P1 | Modelo DB `conversation` + setup SQLAlchemy | P0 anterior |
| P1 | Servicio de logging de conversaciones | P1 DB |
| P2 | Agente Lead (crear, listar, cambiar estado) | P1 router |
| P2 | Agente Propiedad (crear, asociar lead) | P2 lead |
| P2 | Flujo multi-turno (estado de conversación) | P2 agentes |
| P3 | Pruebas unitarias (handlers, router, agentes) | P2 |
| P3 | Pruebas de integración | P3 unit |
| P3 | Dockerizar (Dockerfile + compose) | P0 |

## Secuencia de implementación

```
Semana 1: P0 (base del proyecto + handlers básicos + auth)
Semana 2: P1 (router + DB + logging)
Semana 3: P2 (agentes lead + propiedad + multi-turno)
Semana 4: P3 (tests + docker)
```

## Riesgos

- Dependencia del token de Telegram (hay que pedirlo al operador)
- La clasificación por regex puede ser imprecisa al inicio (mejorable después con LLM)
