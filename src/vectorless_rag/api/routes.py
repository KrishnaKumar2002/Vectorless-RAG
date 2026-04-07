"""API routes."""
from typing import List, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from pydantic import BaseModel
from vectorless_rag.api.dependencies import get_openai_client, get_pageindex_client
from vectorless_rag.retrieval.search import llm_tree_search
from vectorless_rag.retrieval.nodes import build_context
from vectorless_rag.generation.answer import generate_answer
from vectorless_rag.core.tree import create_node_mapping, find_nodes_by_ids
from vectorless_rag.core.clients import pageindex_client
import tempfile
import os


router = APIRouter()


class QueryRequest(BaseModel):
    query: str
    doc_id: str
    expert_rules: str = ""


class QueryResponse(BaseModel):
    answer: str
    node_ids: List[str]
    thinking: str


@router.post("/rag/query", response_model=QueryResponse)
async def rag_query(
    request: QueryRequest,
    pi_client=Depends(get_pageindex_client),
):
    """Full Vectorless RAG pipeline."""
    # Get tree
    tree_result = await pi_client.get_tree(request.doc_id)
    tree = tree_result["result"]

    # Tree search
    search_result = await llm_tree_search(
        request.query,
        tree,
        request.expert_rules,
    )
    node_ids = search_result["node_list"]

    # Retrieve nodes
    node_map = create_node_mapping(tree)
    nodes = [node_map[nid] for nid in node_ids if nid in node_map]

    # Generate answer
    answer = await generate_answer(request.query, nodes)

    return QueryResponse(
        answer=answer,
        node_ids=node_ids,
        thinking=search_result["thinking"],
    )


@router.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    """Upload PDF and return doc_id."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    try:
        result = await pageindex_client.submit_document(tmp_path)
        doc_id = result["doc_id"]
        return {"doc_id": doc_id}
    finally:
        os.unlink(tmp_path)

