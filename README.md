﻿# Chat Website

https://github.com/user-attachments/assets/060dfb0c-61e6-4376-9fbc-3f16de792692

This web application, built with Django, allows users to input prompts and receive a relevant title along with generated Python code based on the input. Powered by [Ollama](https://ollama.com) running locally and utilizing the **Ollama 3.1 model**, the app leverages advanced natural language processing to provide accurate, tailored code snippets.

Whether you need help with coding tasks, algorithms, or script generation, simply describe your prompt — and the app will deliver a solution within seconds!

---

## Requirements

- Python 3.10+
- Docker and Docker Compose (if running with containers)
- Ollama installed locally
- Ollama 3.1 model downloaded

---

## Setup Instructions

### 1. Install Ollama

Follow the [Ollama installation guide](https://ollama.com) for your operating system.

After installation, download the **Ollama 3.1 model**:

```bash
ollama run ollama3.1
```

To run the Ollama server:

```bash
ollama serve
```

---

### 2. Clone the Repository

```bash
git clone https://github.com/Esataydin/chatwebsite.git
cd chatwebsite
```

---

## Running the App

### Option 1: Run Locally (Python)

1. Create and activate a virtual environment:

```bash
python -m venv env
.\env\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

> ⚠️ **Important:**  
> This project is configured for Docker by default.  
> To run locally, you must uncomment two lines:

- In `chatbox/ollama_client.py`, Line 14:
  ```python
  OLLAMA_BASE_URL = "http://localhost:11434"
  ```
- In `chatbox/views.py`, Line 12:
  ```python
  OLLAMA_BASE_URL = "http://localhost:11434"
  ```

3. Run the server:

```bash
python manage.py runserver
```

Access it at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### Option 2: Run with Docker Compose

Build and start the containers:

```bash
docker compose up
```

Access the app at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Notes

- Ensure Ollama is running before starting the app.

---
