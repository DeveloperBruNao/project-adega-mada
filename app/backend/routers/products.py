"""
product.py
Módulo responsável pelas rotas de produtos da API.
"""

from fastapi import APIRouter
from app.backend.models import Produto

router = APIRouter()

produtos = []  # Lista simulando o banco de dados

@router.get("/")
def listar_produtos():
    """
    Retorna a lista de produtos.
    """
    return produtos

@router.post("/")
def adicionar_produto(produto: Produto):
    """
    Adiciona um novo produto à lista.
    """
    produtos.append(produto)
    return {"message": "Produto adicionado com sucesso!", "produto": produto}
