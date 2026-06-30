# Plan de Implementación — Feature 002

## Prioridades

| Prioridad | Tarea | Dependencias |
|---|---|---|
| P0 | Cliente HTTP asíncrono para API Inmovilla + settings | — |
| P0 | Integrar creación de leads → Inmovilla | P0 client |
| P1 | Comando `/buscarcliente` + handler | P0 client |
| P1 | Comando `/sincronizar` propiedades | P0 client |
| P2 | Pruebas unitarias (mock de API) | P1 |

## Secuencia de implementación

```
Paso 1: settings + inmovilla_client.py (HTTP client with Token auth, rate limit)
Paso 2: Modificar lead_agent para crear cliente en Inmovilla al guardar lead
Paso 3: Handler /buscarcliente + servicio de búsqueda
Paso 4: Handler /sincronizar + servicio de importación de propiedades
Paso 5: Tests
```

## Riesgos

- Token de Inmovilla no disponible durante desarrollo → modo "simulado" (log sin llamada real)
- Rate limiting puede causar lentitud si se hacen muchas peticiones seguidas
- La API REST de Inmovilla puede tener diferencias con la documentación
