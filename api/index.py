from app import app
from vercel_wsgi import handle

def handler(environ, start_response):
    return handle(app, environ, start_response)
