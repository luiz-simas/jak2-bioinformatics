import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Configurações do Llama e Ollama
OLLAMA_MODEL = "llama3"
OLLAMA_URL = "http://localhost:11434"

# Caminhos do projeto
PDB_DIR = os.path.join(BASE_DIR, "data", "pdb")
VECTOR_DB_DIR = os.path.join(BASE_DIR, "data", "vector_db")
REPORTS_DIR = os.path.join(BASE_DIR, "data", "reports")

for folder in [PDB_DIR, VECTOR_DB_DIR, REPORTS_DIR]:
    os.makedirs(folder, exist_ok=True)
