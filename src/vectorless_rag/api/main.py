"""FastAPI main app."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from vectorless_rag.api.routes import router
from vectorless_rag.logger import logger


app = FastAPI(
    title="Vectorless RAG API",
    description="Production Vectorless RAG with PageIndex",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/v1")

@app.get("/health")
async def health():
    logger.info("Health check")
    return {"status": "healthy"}

