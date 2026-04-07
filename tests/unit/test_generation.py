"""Unit tests for generation."""
import pytest
from vectorless_rag.generation.answer import generate_answer


@pytest.mark.asyncio
@pytest.mark.unit
async def test_generate_answer(mock_openai_client):
    nodes = [{"title": "Test", "text": "test content"}]
    answer = await generate_answer("test query", nodes)
    assert isinstance(answer, str)
    assert len(answer) > 0

