"""Unit tests for retrieval."""
import pytest
from unittest.mock import AsyncMock
from vectorless_rag.retrieval.search import llm_tree_search
from vectorless_rag.core.tree import TreeNode


@pytest.mark.asyncio
@pytest.mark.unit
async def test_llm_tree_search(mock_openai_client):
    tree: List[TreeNode] = [{"node_id": "0001", "title": "Test"}]
    result = await llm_tree_search("test query", tree)
    assert "node_list" in result
    assert isinstance(result["node_list"], list)

