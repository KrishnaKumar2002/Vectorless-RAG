"""Dependency injection."""
from fastapi import Depends
from vectorless_rag.core.clients import openai_client, pageindex_client


def get_openai_client():
    return openai_client


def get_pageindex_client():
    return pageindex_client

