import requests
from config import MODEL

OLLAMA_URL = "http://91.107.203.23:11434/api/chat"

def llm_decide(latency):

    prompt = f"""
You are a Kubernetes SRE agent.

If latency > 0.5 seconds → SCALE_DEPLOYMENT
If latency normal → DO_NOTHING

Latency: {latency}

Return only action.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }
    )

    return response.json()["message"]["content"].strip()