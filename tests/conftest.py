import pytest


@pytest.fixture
def sample_user_id() -> int:
    return 123456789


@pytest.fixture
def sample_lead_text() -> str:
    return "nuevo cliente interesado en comprar piso"


@pytest.fixture
def sample_property_text() -> str:
    return "quiero registrar una nueva propiedad"
