"""CLI interface."""
import asyncio
import typer
from pathlib import Path
from vectorless_rag.core.clients import pageindex_client
from vectorless_rag.api.main import app  # for uvicorn


app_cli = typer.Typer()


@app_cli.command()
def upload(pdf_path: Path):
    """Upload PDF and get doc_id."""
    result = asyncio.run(pageindex_client.submit_document(str(pdf_path)))
    typer.echo(f"Doc ID: {result['doc_id']}")


@app_cli.command()
def serve(host: str = "0.0.0.0", port: int = 8000):
    """Run API server."""
    import uvicorn
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    app_cli()

