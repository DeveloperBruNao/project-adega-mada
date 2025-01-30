import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.backend.routers import products, opinions

app = FastAPI(
    title="Adega API",
    description="API para gerenciar os produtos e opiniões da adega.",
    version="1.0"
)

# Caminho correto para os arquivos estáticos dentro de frontend/static/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Obtém a pasta `app/`
STATIC_DIR = os.path.join(BASE_DIR, "../frontend/static")  # Caminho correto

# Montando os arquivos estáticos
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.mount("/", StaticFiles(directory=os.path.join(STATIC_DIR, "html"), html=True), name="html")

# Incluindo rotas principais
app.include_router(products.router, prefix="/produtos", tags=["Produtos"])
app.include_router(opinions.router, prefix="/opiniao", tags=["Opiniões"])

@app.get("/api")
def root():
    return {"message": "Bem-vindo à API da Adega!"}
