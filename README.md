# Vectorless-RAG

Production-grade Vectorless RAG implementation using PageIndex.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-Pytest-green)](https://pytest.org/)

## Overview

Tree-based reasoning RAG without vector DB or chunking. LLM navigates document structure for precise retrieval.

## Quick Start

```bash
git clone https://github.com/yourusername/Vectorless-RAG.git
cd Vectorless-RAG
make install
make dev
```

## Architecture

```
src/
├── core/          # Tree building, LLM clients
├── retrieval/     # Tree search, node retrieval
├── generation/    # Answer synthesis
├── api/           # FastAPI server
└── config/        # Settings
```

## Features

- Production FastAPI server
- Async processing
- Docker deployment
- Observability (logging, metrics)
- Tests (90%+ coverage)
- Expert-guided retrieval
- Local & cloud modes

See [DEVELOPMENT.md](DEVELOPMENT.md) for setup.

