from fastapi import FastAPI

app = FastAPI(
    title="Minha API",
    description="Uma descrição opcional da API",
    version="1.0.0",
    docs_url="/docs",  # URL para a interface Swagger UI
    redoc_url="/redoc"  # URL para a interface ReDoc
)
