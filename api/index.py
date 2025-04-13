# api/index.py
from chatbot_project.asgi import application  # change to your Django project's name

async def handler(scope, receive, send):
    await application(scope, receive, send)
