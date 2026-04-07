# Vectorless-RAG Production Implementation TODO

## Approved Plan Steps (Breakdown)

### Phase 1: Core Infrastructure (Current)
- [x] Initial files: README, .gitignore, pyproject.toml
- [ ] Create directory structure: src/, tests/, docker/, configs/, docs/
- [ ] Update pyproject.toml with full deps
- [ ] Create .env.example, Makefile, pytest.ini

### Phase 2: Core Modules
- [ ] src/vectorless_rag/__init__.py (version)
- [ ] src/vectorless_rag/config.py (PydanticSettings)
- [ ] src/vectorless_rag/logger.py (structlog)
- [ ] src/vectorless_rag/core/clients.py (async clients w/ retries)
- [ ] src/vectorless_rag/core/tree.py (compress, node_map)
- [ ] src/vectorless_rag/retrieval/search.py (llm_tree_search async)
- [ ] src/vectorless_rag/retrieval/nodes.py (find_nodes)
- [ ] src/vectorless_rag/generation/answer.py (generate_answer)
- [ ] src/vectorless_rag/cli.py (typer CLI)

### Phase 3: API Server
- [ ] src/vectorless_rag/api/dependencies.py (DI)
- [ ] src/vectorless_rag/api/main.py (FastAPI app)
- [ ] src/vectorless_rag/api/routes.py (endpoints)

### Phase 4: Testing
- [ ] tests/conftest.py (mocks)
- [ ] tests/unit/test_retrieval.py
- [ ] tests/unit/test_generation.py
- [ ] tests/integration/test_api.py
- [ ] Run pytest, coverage >90%

### Phase 5: Deployment
- [ ] docker/Dockerfile
- [ ] docker/docker-compose.yml
- [ ] configs/log.toml
- [ ] docs/api.md (OpenAPI)

### Phase 6: Git & Finalize
- [ ] git checkout -b blackboxai/vectorless-rag-prod
- [ ] git add . && git commit -m "Production Vectorless RAG"
- [ ] git push origin blackboxai/vectorless-rag-prod

**Next Step: Phase 1 complete → Phase 2**

