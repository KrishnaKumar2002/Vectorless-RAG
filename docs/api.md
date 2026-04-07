# API Documentation

## /v1/rag/query
POST - Perform Vectorless RAG

Body:
```json
{
  "query": "What is LLM finetuning?",
  "doc_id": "pi-xxx",
  "expert_rules": "optional rules"
}
```

## /v1/documents/upload
POST - Upload PDF (multipart/form-data, file=pdf)

Returns doc_id for queries.

