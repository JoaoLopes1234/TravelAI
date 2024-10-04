from server import app
from flask import render_template, request, redirect, url_for
from request_Chat_Gpt import *

@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/process', methods=["POST"])
def process():
    prompt = request.form["prompt"]
    response =  answer(prompt)
    return redirect(url_for('result', prompt=response))


@app.route('/result')
def result():
    prompt = request.args.get('prompt')
    return render_template("homepage.html", prompt=prompt)
                    
