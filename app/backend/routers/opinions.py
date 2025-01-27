"""
opinions.py
Módulo responsável pelas rotas de opiniões da API.
"""

from fastapi import APIRouter
from app.backend.models import Opiniao

router = APIRouter()

opinioes = []  # Lista simulando o banco de dados

@router.get("/")
def listar_opinioes():
    """
    Retorna a lista de opiniões.
    """
    return opinioes

@router.post("/")
def adicionar_opiniao(opiniao: Opiniao):
    """
    Adiciona uma nova opinião à lista.
    """
    opinioes.append(opiniao)
    return {"message": "Opinião adicionada com sucesso!", "opiniao": opiniao}
