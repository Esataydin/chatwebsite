import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

def wait_for_ollama(max_retries=5, wait_seconds=3):
    """
    Wait until the Ollama server is available, and pull the required model.
    """
    
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")
    # OLLAMA_BASE_URL = "http://localhost:11434" # For testing
    
    MODEL_NAME = "llama3.1"
    # MODEL_NAME = "llama3.2:1b" # For testing

    # Step 1: Wait for Ollama to be available
    for attempt in range(1, max_retries + 1):
        try:
            print(f"[Ollama Check] Attempt {attempt}: Connecting to {OLLAMA_BASE_URL}")
            response = requests.get(f"{OLLAMA_BASE_URL}/api/tags")
            if response.status_code == 200:
                print("✅ Ollama is ready!")
                break
            else:
                print(f"⚠️ Unexpected response status: {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"❌ Connection failed, retrying in {wait_seconds} seconds...")

        time.sleep(wait_seconds)
    else:
        raise RuntimeError(f"❗ Cannot connect to Ollama at {OLLAMA_BASE_URL} after {max_retries} attempts.")

    # Step 2: Pull the model if needed
    pull_model(OLLAMA_BASE_URL, MODEL_NAME)


def pull_model(base_url, model_name):
    """
    Pull the required model into Ollama.
    """
    print(f"📦 Checking if model '{model_name}' is available...")

    # Check if model already exists
    try:
        response = requests.get(f"{base_url}/api/tags")
        response.raise_for_status()
        tags = response.json().get("models", [])

        if any(model.get("name") == model_name for model in tags):
            print(f"✅ Model '{model_name}' is already available!")
            return
    except Exception as e:
        print(f"⚠️ Failed to check existing models: {e}")

    # Pull the model if not available
    print(f"⬇️ Pulling model '{model_name}' from Ollama...")
    try:
        response = requests.post(f"{base_url}/api/pull", json={"name": model_name}, stream=True)
        response.raise_for_status()
        
        # Stream the pull progress (optional)
        for line in response.iter_lines():
            if line:
                print(line.decode('utf-8'))
        
        print(f"✅ Model '{model_name}' pulled successfully!")
    except Exception as e:
        raise RuntimeError(f"❗ Failed to pull model '{model_name}': {e}")
