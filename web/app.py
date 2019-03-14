"""
Web application for the Text Scramble test.

@author: Gus Garcia
@date: 15/03/2019
"""
from scramble import scramble_text as st
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/code")
def scramble_code():
    return render_template("index.html")


@app.route("/scramble", methods=['POST'])
def scramble():
    text = request.form["text"]
    return "".join(reversed(text))
