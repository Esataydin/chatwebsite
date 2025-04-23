from django.shortcuts import render, redirect

import ollama
import json

base_prompt = "DO NOT OUTPUT ANYTHING OTHER THAN THESE GIVEN INSTRUCTIONS!: Only output in the format as follows: \"[related title for given prompt]|||[python code for given prompt]\". Prompt: "

def home(request):
    return redirect("input")

def input_view(request):
    if request.method == 'POST':
        prompt = base_prompt + request.POST["prompt"]
        request.session["prompt"] = prompt
        return redirect("output")
    return render(request, "chatbox/input.html")


def output_view(request):
    client = ollama.Client()
    model = "llama3.1"
    prompt = request.session["prompt"]
    
    response = client.generate(model=model, prompt=prompt)
    response_text = response.response
    
    response_list = response_text.split("|||")
    title = response_list[0]
    code_block = response_list[1].replace("```python", "").replace("```", "").split("\n")
    
    return render(request, 'chatbox/output.html', {
        'title': title,
        'code_block': code_block
    })