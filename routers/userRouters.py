from flask import Flask, Blueprint

url = Blueprint('userRouters', __name__)


@url.route("/")
def hello_world():
    return "<p>Hello, World!</p>"