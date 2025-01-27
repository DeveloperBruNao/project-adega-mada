from pydantic import BaseModel

# Modelo que representa um produto
class Produto(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float
    estoque: int

# Modelo que representa uma opinião
class Opiniao(BaseModel):
    id: int
    cliente: str
    comentario: str
    nota: int
