"""Node retrieval utilities."""
from typing import List
from vectorless_rag.core.tree import TreeNode, find_nodes_by_ids, create_node_mapping
from vectorless_rag.logger import logger


def build_context(nodes: List[TreeNode]) -> str:
    """Build context string from nodes."""
    if not nodes:
        return "No relevant sections found."
    
    parts = []
    for node in nodes:
        title = node["title"]
        page = node.get("page_index", "?")
        text = node.get("text", "")
        parts.append(f"[Section: '{title}' | Page {page}]\\n{text}")
    
    context = "\\n\\n---\\n\\n".join(parts)
    logger.info("Context built", node_count=len(nodes), chars=len(context))
    return context

