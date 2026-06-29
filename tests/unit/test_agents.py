import pytest

from src.agents.lead_agent import LeadAgent
from src.agents.property_agent import PropertyAgent
from src.agents.marketing_agent import MarketingAgent


@pytest.mark.asyncio
async def test_lead_agent_response(sample_user_id):
    agent = LeadAgent()
    response = await agent.handle("nuevo cliente", sample_user_id)
    assert "Lead" in response
    assert "nombre" in response.lower()


@pytest.mark.asyncio
async def test_property_agent_response(sample_user_id):
    agent = PropertyAgent()
    response = await agent.handle("nueva propiedad", sample_user_id)
    assert "Propiedad" in response
    assert "dirección" in response.lower()


@pytest.mark.asyncio
async def test_marketing_agent_response(sample_user_id):
    agent = MarketingAgent()
    response = await agent.handle("publicar", sample_user_id)
    assert "Marketing" in response
