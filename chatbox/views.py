from django.shortcuts import render, redirect
from django.http import HttpResponse

import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
# OLLAMA_BASE_URL = "http://localhost:11434" # For testing
MODEL_NAME = "llama3.1"
# MODEL_NAME = "llama3.2:1b" # For testing

BASE_PROMPT = "DO NOT OUTPUT ANYTHING OTHER THAN THESE GIVEN INSTRUCTIONS!: Only output in the format as follows: \"[related title for given prompt]|||[python code for given prompt]\". Prompt: "


def home(request):
    return redirect("input")

def input_view(request):
    if request.method == 'POST':
        prompt = BASE_PROMPT + request.POST["prompt"]
        request.session["prompt"] = prompt
        return redirect("output")
    return render(request, "chatbox/input.html")


def output_view(request):

    
    prompt = request.session["prompt"]
    
    body = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(OLLAMA_BASE_URL + "/api/generate", data=json.dumps(body))
    response_text = response.json()['response']
    response_list = response_text.split("|||") # for medium models
    # response_list = response_text.split("|") # for small models # Testing
    
    print("\n")
    print(response_text)
    print("\n")
    
    title = response_list[0]
    for index in range(1, 5):
        try:
            code_block = response_list[index]
            if code_block != "":
                break
        except:
            return HttpResponse(status=500)
        
    code_block = code_block.replace("```python", "").replace("```", "").split("\n")
    
    return render(request, 'chatbox/output.html', {
        'title': title,
        'code_block': code_block
    })