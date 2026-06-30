# Tareas — Feature 002

## Tarea 002.1 — Cliente HTTP Inmovilla

**Issue**: `[FEAT-002.1] Cliente HTTP para API REST de Inmovilla`

**Checklist**:
- [ ] Agregar `INMOVILLA_TOKEN` y `INMOVILLA_NUMAGENCIA` a settings.py
- [ ] Crear `src/services/inmovilla_client.py` con clase asíncrona
- [ ] Implementar métodos: `create_client`, `get_client`, `search_client`, `list_properties`, `get_property`
- [ ] Implementar rate limiting (2 req/min enums, 20 req/min resto)
- [ ] Manejo de errores HTTP (408 → esperar y reintentar)

**Criterios de aceptación**:
- El cliente se puede instanciar con o sin token (modo simulado)
- Las peticiones se hacen con httpx.AsyncClient
- Si el token no está configurado, loguea warning y no lanza excepción

**Dependencias**: Ninguna

---

## Tarea 002.2 — Sincronización de Leads

**Issue**: `[FEAT-002.2] Crear cliente en Inmovilla al registrar lead`

**Checklist**:
- [ ] Modificar `src/agents/lead_agent.py` para llamar a `inmovilla_client.create_client()` después de guardar lead
- [ ] Guardar `inmovilla_cod_cli` en el lead local
- [ ] Agregar campo `inmovilla_cod_cli` al modelo Lead
- [ ] Si falla, loguear error y marcar lead como `sync_pending`

**Criterios de aceptación**:
- Al crear lead con datos válidos, se crea cliente en Inmovilla
- El `cod_cli` de Inmovilla queda registrado en el lead local
- Si Inmovilla no responde, el lead se crea igual con estado `sync_pending`

**Dependencias**: 002.1

---

## Tarea 002.3 — Búsqueda de clientes

**Issue**: `[FEAT-002.3] Comando /buscarcliente + handler`

**Checklist**:
- [ ] Agregar comando `/buscarcliente` al router de Telegram
- [ ] Implementar handler que recibe teléfono o nombre
- [ ] Llamar a `inmovilla_client.search_client()` y mostrar resultados
- [ ] Formatear respuesta con datos del cliente

**Criterios de aceptación**:
- `/buscarcliente 666554433` busca y muestra resultados
- Si no hay resultados, mensaje claro
- Si no hay token configurado, mensaje informativo

**Dependencias**: 002.1

---

## Tarea 002.4 — Sincronización de propiedades

**Issue**: `[FEAT-002.4] Comando /sincronizar para importar propiedades`

**Checklist**:
- [ ] Agregar comando `/sincronizar` al router de Telegram
- [ ] Implementar servicio que llama a `list_properties` con paginación
- [ ] Guardar/actualizar propiedades en tabla local
- [ ] Evitar duplicados por `cod_ofer`
- [ ] Mostrar resumen: "Se importaron X propiedades nuevas, Y actualizadas"

**Criterios de aceptación**:
- `/sincronizar` importa propiedades desde Inmovilla
- Las propiedades existentes se actualizan (no duplican)
- El bot responde con resumen de la operación

**Dependencias**: 002.1

---

## Tarea 002.5 — Tests

**Issue**: `[FEAT-002.5] Tests de integración Inmovilla`

**Checklist**:
- [ ] Mock de respuestas de Inmovilla API con respuestas.json de ejemplo
- [ ] Test: crear lead → llama a create_client
- [ ] Test: buscar cliente → parsea respuesta correctamente
- [ ] Test: rate limiting → no excede límites
- [ ] Test: sin token → no lanza excepción

**Criterios de aceptación**:
- Tests unitarios con httpx mock
- Sin dependencia de red
- Cobertura de casos error

**Dependencias**: 002.2, 002.3, 002.4
