# JAK2 V617F Bioinformatics & Screening Platform

An autonomous platform for clinical analysis of the **JAK2 V617F mutation**, molecular screening (HTVS), and AI-assisted consultation powered by a local **Llama 3 RAG** pipeline (Ollama).

Built with Python, Streamlit, and FastAPI.

## Modules

- **Clinical & Hematology Analysis** (`modules/hematology_rules.py`) — rule-based evaluation of JAK2 V617F status against a full blood panel (hemoglobin, hematocrit, platelets, leukocytes), with automated risk flags.
- **Molecular Screening / HTVS** (`modules/docking.py`, `modules/admet.py`) — virtual screening workflow with a Lipinski (rule-of-five) ADMET filter for candidate compounds.
- **Llama RAG Consultation** (`modules/llama_engine.py`) — retrieval-augmented Q&A over a local vector store, served by Ollama (Llama 3) running entirely on-device — no external API keys, no patient data leaves the machine.
- **API service** (`api.py`) — the same engines exposed as REST endpoints with FastAPI + Pydantic.

## Run it

```bash
pip install -r requirements.txt

# Web interface (Streamlit)
streamlit run app.py

# Optional: API service (FastAPI)
uvicorn api:app --reload
```

For the RAG module, run [Ollama](https://ollama.com) locally with the `llama3` model pulled. Data folders (`data/pdb`, `data/vector_db`, `data/reports`) are created automatically on first run.

## Tech

Python · Streamlit · FastAPI · Pydantic · Ollama / Llama 3 · RAG (vector store) · rule-based clinical engines

## Notes

Research/educational project — not a medical device and not a substitute for clinical diagnosis. Interface is in Portuguese (pt-BR); see `README.pt-BR.md` for the original readme.
