"""Pytest fixtures."""
import pytest
from unittest.mock import AsyncMock, MagicMock
import pytest_asyncio


@pytest_asyncio.fixture
def mock_openai_client():
    client = AsyncMock()
    client.chat.return_value = MagicMock(choices=[MagicMock(message=MagicMock(content='{"thinking": "test", "node_list": ["0001"]}'))])
    return client


@pytest_asyncio.fixture
def mock_pageindex_client():
    client = MagicMock()
    client.get_tree.return_value = {"result": [{"node_id": "0001", "title": "Test", "text": "test content", "page_index": 1}]}
    return client

