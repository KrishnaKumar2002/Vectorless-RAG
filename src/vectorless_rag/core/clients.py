 chan"""Async LLM and PageIndex clients."""
import asyncio
from typing import Dict, Any, List
from functools import wraps
from tenacity import retry, stop_after_attempt, wait_exponential
import httpx
from openai import AsyncOpenAI
from pageindex import PageIndexClient
from vectorless_rag.config import settings
from vectorless_rag.logger import logger


class RetryClient:
    """Base client with retries."""

    @retry(stop=stop_after_attempt(settings.max_retries), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def _request(self, *args, **kwargs):
        raise NotImplementedError


class OpenAIClient(RetryClient):
    """Async OpenAI client."""

    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)

    async def chat(self, messages: List[Dict[str, str]], model: str = None, **kwargs) -> Dict[str, Any]:
        """Chat completion."""
        model = model or settings.openai_model
        logger.info("Calling OpenAI", model=model, msg_len=len(messages))
        response = await self.client.chat.completions.create(
            model=model,
            messages=messages,
            **kwargs,
        )
        logger.info("OpenAI response received")
        return response


class PageIndexAsyncClient:
    """Async wrapper for PageIndexClient (sync)."""

    def __init__(self):
        self.client = PageIndexClient(api_key=settings.pageindex_api_key)

    async def submit_document(self, pdf_path: str) -> Dict[str, Any]:
        """Upload PDF async."""
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, self.client.submit_document, pdf_path)
        return result

    async def get_tree(self, doc_id: str, node_summary: bool = True) -> Dict[str, Any]:
        """Get tree async."""
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, self.client.get_tree, doc_id, node_summary)
        return result

    async def get_document(self, doc_id: str) -> Dict[str, Any]:
        """Get document status."""
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, self.client.get_document, doc_id)
        return result

    async def chat_completions(self, messages: List[Dict[str, str]], doc_id: str) -> Dict[str, Any]:
        """Chat API."""
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, self.client.chat_completions, messages, doc_id)
        return result


openai_client = OpenAIClient()
pageindex_client = PageIndexAsyncClient()

