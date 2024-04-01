from flask import Flask
from routers import userRouters # Import the Routers folder and access urls

app = Flask(__name__)

app.register_blueprint(userRouters.url, url_prefix = "/api/v1/")

