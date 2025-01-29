from fastapi import APIRouter, HTTPException
from app.backend.models import Produto
from app.backend.database import DB_NAME
import sqlite3

router = APIRouter()

# Lista de produtos simulando um banco de dados
produtos = []  # Temporário, caso queira ainda usar a lista em memória

@router.post("/")
def criar_produto(produto: Produto):
    """
    Cadastra um novo produto no banco de dados.
    """
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO produtos (nome, descricao, preco, estoque)
        VALUES (?, ?, ?, ?)
    ''', (produto.nome, produto.descricao, produto.preco, produto.estoque))

    conexao.commit()
    produto_id = cursor.lastrowid  # Obtém o ID gerado automaticamente pelo banco
    conexao.close()

    return {"message": "Produto cadastrado com sucesso!", "id": produto_id}


@router.get("/")
def listar_produtos():
    """
    Retorna a lista de todos os produtos cadastrados no banco de dados.
    """
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome, descricao, preco, estoque FROM produtos")
    produtos = [
        {"id": row[0], "nome": row[1], "descricao": row[2], "preco": row[3], "estoque": row[4]}
        for row in cursor.fetchall()
    ]

    conexao.close()
    return produtos

@router.put("/{produto_id}")
def atualizar_produto(produto_id: int, produto_atualizado: Produto):
    """
    Atualiza as informações de um produto existente no banco de dados.
    """
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    # Verifica se o produto existe
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,))
    produto_existente = cursor.fetchone()

    if not produto_existente:
        conexao.close()
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    # Atualiza os dados do produto
    cursor.execute('''
        UPDATE produtos
        SET nome = ?, descricao = ?, preco = ?, estoque = ?
        WHERE id = ?
    ''', (produto_atualizado.nome, produto_atualizado.descricao, produto_atualizado.preco, produto_atualizado.estoque, produto_id))

    conexao.commit()
    conexao.close()

    return {"message": "Produto atualizado com sucesso", "produto": produto_atualizado}
