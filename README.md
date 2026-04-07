# Vectorless-RAG

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-Pytest-green)](https://pytest.org/)

Production-grade implementation of **Vectorless RAG** using [PageIndex](https://pageindex.ai) - reasoning-based retrieval without vector databases or arbitrary chunking.

**Live Demo:** https://github.com/KrishnaKumar2002/Vectorless-RAG/tree/blackboxai/vectorless-rag-prod

## 🎯 How Vectorless RAG Works Internally

Traditional Vector RAG fails on complex documents because **similarity ≠ relevance**. A chunk mentioning \"risks\" might match higher than the actual EBITDA section.

**Vectorless RAG Pipeline (4 Steps):**

```
1. UPLOAD PDF → PageIndex LLM builds TREE INDEX
   ├── Preface (p1)
   │  └── Module 1 (p4)
   └── Modern LLMs Finetuning (p12)
      ├── PEFT (p13)
      └── RLHF (p13)

2. QUERY + TREE → LLM Tree Search (gpt-4o-mini)
   Query: \"LLM finetuning syllabus?\"
   LLM reasons: \"Check 'Modern LLMs Finetuning' node 0010 & children\"
   → Returns: [\"0010\", \"0014\", \"0015\"]

3. RETRIEVE Nodes → Exact sections with titles/pages
   [Section: 'PEFT' | p13]
   LoRA, QLoRA, DoRA...

4. GENERATE Answer → Grounded response with citations
   \"PEFT includes LoRA... (PEFT, p13)\"
```

**Advantages:**
- **98.7% FinanceBench** vs ~80% vector RAG
- **Traceable**: Node IDs, pages, titles
- **Expert Rules**: Domain knowledge via prompts (no fine-tuning)
- **No Infra**: JSON tree vs Pinecone/Chroma

## 🚀 Quick Start

```bash
git clone https://github.com/KrishnaKumar2002/Vectorless-RAG.git -b blackboxai/vectorless-rag-prod
cd Vectorless-RAG

# Setup
cp .env.example .env
# Add PAGEINDEX_API_KEY (dash.pageindex.ai) & OPENAI_API_KEY

pip install -e .
uvicorn vectorless_rag.api.main:app --reload
```

**API Endpoints:** http://localhost:8000/docs

```
# 1. Upload PDF
curl -X POST \"/v1/documents/upload\" -F \"file=@your.pdf\"

# 2. Query (wait for processing ~30s)
curl -X POST \"/v1/rag/query\" \\
  -H \"Content-Type: application/json\" \\
  -d '{\"query\": \"LLM finetuning syllabus?\", \"doc_id\": \"pi-xxx\"}'
```

**CLI:**
```bash
vectorless-rag upload sample.pdf
vectorless-rag serve
```

## 🏗️ Architecture (SOLID/12-Factor)

```
src/vectorless_rag/
├── config.py      # PydanticSettings (.env)
├── logger.py      # structlog (JSON, trace_id)
├── core/          # AsyncOpenAI + PageIndexClient (retries)
│   ├── clients.py
│   └── tree.py    # compress_tree, find_nodes_by_ids
├── retrieval/     # llm_tree_search (jinja prompts)
│   ├── search.py
│   └── nodes.py
├── generation/    # generate_answer (cited)
│   └── answer.py
├── api/           # FastAPI (DI, CORS, health)
│   └── routes.py  # /v1/rag/query, /documents/upload
└── cli.py         # typer CLI
```

**Principles Applied:**
- **SRP**: Single responsibility modules
- **DI**: FastAPI Depends for clients
- **Async**: All LLM I/O concurrent
- **Observability**: Request logging w/ contextvars
- **Robust**: Tenacity retries, validation

## 🧪 Tests (80%+ Coverage Ready)

```bash
pip install -e '.[dev]'
pytest --cov=vectorless_rag  # unit/integration
```

Tests: mock LLM responses, tree parsing, answer generation.

## 📦 Deployment

```bash
docker-compose up  # Full stack
```

**Dockerfile** multi-stage, .venv ignored.

## 📚 Resources & Acknowledgements

**Core Innovation:** [PageIndex](https://pageindex.ai) by VectifyAI - cloud tree indexing service.
- SDK: `pip install pageindex`
- API Keys: https://dash.pageindex.ai/api-keys
- Open Source: https://github.com/VectifyAI/PageIndex
- Crash Course: Krish Naik (@krishnaik06) notebook inspiration

**Why PageIndex > Vector RAG:**
> \"Similarity ≠ Relevance\" - LLM reasons over document structure like human experts.

**Built With:**
- FastAPI (API), Pydantic (models/config)
- structlog (logging), tenacity (retries)
- pytest-asyncio (tests), typer (CLI)
- Docker (deploy)

## 🔮 Future (TODO.md)
- Redis caching for trees
- Multi-doc search
- Agentic retrieval
- GitHub Actions CI/CD

MIT License. Contributions welcome!


