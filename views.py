from server import app
from flask import render_template, request
from request_Chat_Gpt import *

@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/process', methods=["POST"])
def process():

    data = request.get_json()

    prompt = data.get('prompt', '')
    response =  answer(prompt)
    #return redirect(url_for('result', prompt=response))

    return {"response": response}


@app.route('/result')
def result():
    prompt = request.args.get('prompt')
    return render_template("homepage.html", prompt=prompt)
                    
