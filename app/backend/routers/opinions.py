from fastapi import APIRouter, HTTPException
from app.backend.models import Opiniao
from app.backend.database import DB_NAME
import sqlite3

router = APIRouter()

@router.get("/")
def listar_opinioes():
    """
    Retorna todas as opiniões cadastradas no banco de dados.
    """
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    cursor.execute("SELECT id, cliente, comentario, nota FROM opinioes")
    opinioes = [
        {"id": row[0], "cliente": row[1], "comentario": row[2], "nota": row[3]}
        for row in cursor.fetchall()
    ]

    conexao.close()
    return opinioes

@router.post("/")
def adicionar_opiniao(opiniao: Opiniao):
    """
    Adiciona uma nova opinião no banco de dados.
    """
    if opiniao.nota < 1 or opiniao.nota > 5:
        raise HTTPException(status_code=400, detail="A nota deve estar entre 1 e 5.")

    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO opinioes (cliente, comentario, nota)
        VALUES (?, ?, ?)
    ''', (opiniao.cliente, opiniao.comentario, opiniao.nota))

    conexao.commit()
    opiniao_id = cursor.lastrowid
    conexao.close()

    return {"message": "Opinião adicionada com sucesso!", "id": opiniao_id}

@router.delete("/{opiniao_id}")
def deletar_opiniao(opiniao_id: int):
    """
    Deleta uma opinião do banco de dados.
    """
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM opinioes WHERE id = ?", (opiniao_id,))
    opiniao_existente = cursor.fetchone()

    if not opiniao_existente:
        conexao.close()
        raise HTTPException(status_code=404, detail="Opinião não encontrada")

    cursor.execute("DELETE FROM opinioes WHERE id = ?", (opiniao_id,))
    conexao.commit()
    conexao.close()

    return {"message": "Opinião deletada com sucesso!"}

@router.put("/{opiniao_id}")
def atualizar_opiniao(opiniao_id: int, opiniao_atualizada: Opiniao):
    """
    Atualiza uma opinião existente no banco de dados.
    """
    if opiniao_atualizada.nota < 1 or opiniao_atualizada.nota > 5:
        raise HTTPException(status_code=400, detail="A nota deve estar entre 1 e 5.")

    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM opinioes WHERE id = ?", (opiniao_id,))
    opiniao_existente = cursor.fetchone()

    if not opiniao_existente:
        conexao.close()
        raise HTTPException(status_code=404, detail="Opinião não encontrada")

    cursor.execute('''
        UPDATE opinioes
        SET cliente = ?, comentario = ?, nota = ?
        WHERE id = ?
    ''', (opiniao_atualizada.cliente, opiniao_atualizada.comentario, opiniao_atualizada.nota, opiniao_id))

    conexao.commit()
    conexao.close()

    return {"message": "Opinião atualizada com sucesso!"}
