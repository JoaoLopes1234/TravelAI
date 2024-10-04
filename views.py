from server import app
from flask import render_template, request

@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/process', methods=["POST"])
def process():
    prompt = request.form["prompt"]
    return f'Nome recebido: {prompt}'
