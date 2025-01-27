"""
main.py
Este é o ponto de entrada principal da aplicação FastAPI.
Configura as rotas e inicializa o servidor.
"""
from fastapi import FastAPI
from app.backend.routers import products, opinions

app = FastAPI(
    title="Adega API",
    description="API para gerenciar os produtos e opiniões da adega.",
    version="1.0"
)

# Incluindo rotas principais
app.include_router(products.router, prefix="/produtos", tags=["Produtos"])
app.include_router(opinions.router, prefix="/opiniao", tags=["Opiniões"])

@app.get("/")
def root():
    """
    Rota raiz da aplicação.
    Retorna uma mensagem de boas-vindas.
    """
    return {"message": "Bem-vindo à API da Adega!"}
