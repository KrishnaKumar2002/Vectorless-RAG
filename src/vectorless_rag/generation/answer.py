"""Answer generation."""
from typing import List
from jinja2 import Template
from vectorless_rag.core.clients import openai_client
from vectorless_rag.retrieval.nodes import build_context
from vectorless_rag.logger import logger


ANSWER_PROMPT = """
Answer using ONLY the context. Cite section title and page for every claim.

Question: {{ query }}

Context:
{{ context }}

Answer:
"""


async def generate_answer(
    query: str,
    nodes: List[dict],
) -> str:
    """Generate grounded answer."""
    context = build_context(nodes)
    
    prompt_template = Template(ANSWER_PROMPT)
    prompt = prompt_template.render(query=query, context=context)
    
    messages = [{"role": "user", "content": prompt}]
    response = await openai_client.chat(messages=messages)
    
    answer = response.choices[0].message.content
    logger.info("Answer generated", chars=len(answer))
    return answer

