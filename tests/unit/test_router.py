import pytest

from src.agents.router import classify_intent


@pytest.mark.parametrize(
    "text,expected",
    [
        ("nuevo cliente", "lead"),
        ("registrar cliente potencial", "lead"),
        ("quiero captar leads", "lead"),
        ("nueva propiedad", "property"),
        ("dar de alta un piso", "property"),
        ("casa en venta", "property"),
        ("publicar en redes", "marketing"),
        ("crear anuncio", "marketing"),
        ("promocionar propiedad", "marketing"),
        ("tarea pendiente", "task"),
        ("recordatorio", "task"),
        ("estado del día", "status"),
        ("resumen semanal", "status"),
        ("hola buenos días", "unknown"),
        ("gracias", "unknown"),
        ("", "unknown"),
    ],
)
def test_classify_intent(text: str, expected: str):
    assert classify_intent(text) == expected
