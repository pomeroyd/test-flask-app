from flask import Flask, request
from emoji import emojize 

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return emojize("Hello " + name +"!")


