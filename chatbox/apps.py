from django.apps import AppConfig
from .ollama_client import wait_for_ollama


# class ChatboxConfig(AppConfig):
#     default_auto_field = "django.db.models.BigAutoField"
#     name = "chatbox"

class ChatBoxConfig(AppConfig):
    name = 'chatbox'

    def ready(self):
        wait_for_ollama()