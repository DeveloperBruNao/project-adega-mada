# Adega Project - Configurando o Ambiente Inicial

# Estrutura Inicial do Projeto
# - app/ (Pasta principal)
#   - backend/ (FastAPI)
#     - main.py (Ponto de entrada do backend)
#     - models.py (Modelos do banco de dados)
#     - database.py (Conexão com SQLite)
#     - routers/ (Sub-rotas para organizarmos o backend)
#   - frontend/ (Flask)
#     - app.py (Ponto de entrada do frontend)
#     - templates/ (HTML para o Flask)
#     - static/ (CSS, JS, imagens)
# - docker-compose.yml
# - Dockerfile (Configuração para container)
# - README.md (Documentação)

# Etapa 1: Criando a estrutura de pastas
# (Instrução para criar as pastas manualmente ou via script em um ambiente local.)

import os

def criar_estrutura_projeto():
    pastas = [
        "app/backend/routers",
        "app/frontend/templates",
        "app/frontend/static/css",
        "app/frontend/static/js",
        "app/frontend/static/images"
    ]
    for pasta in pastas:
        os.makedirs(pasta, exist_ok=True)

    # Criar arquivos principais
    arquivos = [
        "app/backend/main.py",
        "app/backend/models.py",
        "app/backend/database.py",
        "app/frontend/app.py",
        "Dockerfile",
        "docker-compose.yml",
        "README.md"
    ]
    for arquivo in arquivos:
        with open(arquivo, "w") as f:
            if "README.md" in arquivo:
                f.write("# Adega Project\n\nDocumentação em progresso...")

if __name__ == "__main__":
    criar_estrutura_projeto()
    print("Estrutura inicial do projeto criada com sucesso!")
