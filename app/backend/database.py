import sqlite3

# Nome do arquivo do banco de dados
DB_NAME = "adega.db"

# Função para criar as tabelas no banco de dados
def criar_tabelas():
    """
    Cria as tabelas 'produtos' e 'opinioes' no banco de dados se não existirem.
    """
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    # Criação da tabela de produtos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL
        )
    ''')

    # Criação da tabela de opiniões
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS opinioes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            comentario TEXT NOT NULL,
            nota INTEGER CHECK(nota >= 1 AND nota <= 5)
        )
    ''')

    # Salva as alterações e fecha a conexão
    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    criar_tabelas()
    print("Banco de dados configurado com sucesso!")
