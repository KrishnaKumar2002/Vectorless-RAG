"""Tree utilities."""
from typing import List, Dict, Any, Union
import json
from vectorless_rag.logger import logger


TreeNode = Dict[str, Any]


def compress_tree(nodes: List[TreeNode], max_chars: int = 150) -> List[Dict[str, Any]]:
    """Compress tree for LLM prompt."""
    compressed = []
    for node in nodes:
        entry = {
            "node_id": node["node_id"],
            "title": node["title"],
            "page": node.get("page_index", "?"),
            "summary": node.get("text", "")[:max_chars],
        }
        if node.get("nodes"):
            entry["children"] = compress_tree(node["nodes"], max_chars)
        compressed.append(entry)
    return compressed


def create_node_mapping(tree: List[TreeNode]) -> Dict[str, TreeNode]:
    """Create node_id -> node mapping."""
    mapping = {}
    for node in tree:
        mapping[node["node_id"]] = node
        if node.get("nodes"):
            mapping.update(create_node_mapping(node["nodes"]))
    return mapping


def find_nodes_by_ids(tree: List[TreeNode], target_ids: List[str]) -> List[TreeNode]:
    """Recursively find nodes by IDs."""
    found = []
    for node in tree:
        if node["node_id"] in target_ids:
            found.append(node)
        if node.get("nodes"):
            found += find_nodes_by_ids(node["nodes"], target_ids)
    return found


def count_nodes(tree: List[TreeNode]) -> int:
    """Count total nodes."""
    total = len(tree)
    for node in tree:
        if node.get("nodes"):
            total += count_nodes(node["nodes"])
    return total

