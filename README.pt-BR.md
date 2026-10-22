# Plataforma de Bioinformática & Triagem JAK2 V617F

Este repositório contém o código completo da plataforma autónoma para análise clínica de JAK2, triagem molecular (HTVS) e integração com Ollama/Llama.

## Como Executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute a interface Streamlit:
   ```bash
   streamlit run app.py
   ```

3. (Opcional) Execute os serviços API com FastAPI:
   ```bash
   uvicorn api:app --reload
   ```
