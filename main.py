from fastapi import FastAPI
from get import router as get_router
from post import router as post_router
from put import router as put_router
from delete import router as delete_router

app = FastAPI()

# Adiciona as rotas separadas
app.include_router(get_router)
app.include_router(post_router)
app.include_router(put_router)
app.include_router(delete_router)
