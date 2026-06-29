import pytest

from src.agents.intent_classifier import classify_intent
from src.agents.lead_agent import LeadAgent
from src.agents.marketing_agent import MarketingAgent
from src.agents.property_agent import PropertyAgent


@pytest.mark.asyncio
async def test_lead_agent_help(sample_user_id):
    agent = LeadAgent()
    response = await agent.handle("nuevo cliente", sample_user_id)
    assert "Lead" in response
    assert "Nombre" in response


@pytest.mark.asyncio
async def test_lead_agent_create(sample_user_id):
    agent = LeadAgent()
    text = "Juan Pérez | 612345678 | juan@email.com | comprador"
    response = await agent.handle(text, sample_user_id)
    assert "Lead" in response or "Error" in response
    # Si no hay DB, esperamos error, no crash


@pytest.mark.asyncio
async def test_property_agent_help(sample_user_id):
    agent = PropertyAgent()
    response = await agent.handle("nueva propiedad", sample_user_id)
    assert "Propiedad" in response or "Propiedades" in response


@pytest.mark.asyncio
async def test_marketing_agent(sample_user_id):
    agent = MarketingAgent()
    response = await agent.handle("publicar", sample_user_id)
    assert "Marketing" in response


@pytest.mark.asyncio
async def test_marketing_description(sample_user_id):
    agent = MarketingAgent()
    text = "Piso centro | Calle Mayor | 180000 | 90 | 3 | 2 | terraza"
    response = await agent.handle(text, sample_user_id)
    assert "Piso centro" in response
    assert "terraza" in response


@pytest.mark.parametrize(
    "text,expected",
    [
        ("nuevo cliente", "lead"),
        ("registrar cliente potencial", "lead"),
        ("nueva propiedad", "property"),
        ("dar de alta un piso", "property"),
        ("publicar en redes", "marketing"),
        ("crear anuncio", "marketing"),
        ("tarea pendiente", "task"),
        ("estado del día", "status"),
        ("hola buenos días", "unknown"),
    ],
)
def test_classify_intent(text, expected):
    assert classify_intent(text) == expected
