"""LLM tree search."""
from typing import List, Dict, Any
from jinja2 import Template
from vectorless_rag.core.clients import openai_client
from vectorless_rag.core.tree import compress_tree
from vectorless_rag.logger import logger


SEARCH_PROMPT_TEMPLATE = """
You are given a query and a document's tree structure (Table of Contents).
Identify node IDs most likely containing the answer.

Query: {{ query }}

{% if expert_rules %}
Expert Rules:
{{ expert_rules }}
{% endif %}

Document Tree:
{{ tree_json }}

Reply ONLY in JSON:
{
  "thinking": "<reasoning>",
  "node_list": ["node_id1", "node_id2"]
}
"""


async def llm_tree_search(
    query: str,
    tree: List[Dict[str, Any]],
    expert_rules: str = "",
    model: str = None,
) -> Dict[str, Any]:
    """Core tree search."""
    compressed_tree = compress_tree(tree)
    tree_json = json.dumps(compressed_tree, indent=2)

    prompt_template = Template(SEARCH_PROMPT_TEMPLATE)
    prompt = prompt_template.render(
        query=query,
        tree_json=tree_json,
        expert_rules=expert_rules,
    )

    messages = [{"role": "user", "content": prompt}]
    response = await openai_client.chat(
        messages=messages,
        model=model,
        response_format={"type": "json_object"},
    )
    
    result = json.loads(response.choices[0].message.content)
    logger.info("Tree search complete", node_count=len(result["node_list"]))
    return result

