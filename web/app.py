"""
Web application for the Text Scramble test.

@author: Gus Garcia
@date: 15/03/2019
"""
from scramble import scramble_text as st
import requests
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


WIKI_URI = ("https://en.wikipedia.org/w/api.php?"
            "action=query&list=search&srsearch=brain&format=json")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/more")
def wikipedia_links():
    wiki_items = requests.get(WIKI_URI).json()
    return render_template("more.html", pages=wiki_items['query']['search'])


@app.route("/scramble", methods=['POST'])
def scramble():
    text = request.form["text"]
    return jsonify("".join(reversed(text)))
