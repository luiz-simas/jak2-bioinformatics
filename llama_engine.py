import requests
from config import OLLAMA_URL, OLLAMA_MODEL

class LlamaEngine:
    def __init__(self, model_name=OLLAMA_MODEL):
        self.model_name = model_name
        self.url = f"{OLLAMA_URL}/api/generate"

    def generate_response(self, prompt: str, system_prompt: str = "") -> str:
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "system": system_prompt,
            "stream": False
        }
        try:
            response = requests.post(self.url, json=payload)
            if response.status_code == 200:
                return response.json().get("response", "")
            return f"Erro no Ollama: Status {response.status_code}"
        except Exception as e:
            return f"Erro de conexão com o Ollama local: {str(e)}"
