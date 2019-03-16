"""
Web application for the Text Scramble test.

@author: Gus Garcia
@date: 15/03/2019
"""
import requests
from flask import Flask, render_template, request, jsonify
from flask import Markup
from scramble.text_scrambler import TextScrambler
app = Flask(__name__)
textScrambler = TextScrambler()


WIKI_URI = ("https://en.wikipedia.org/w/api.php?"
            "action=query&list=search&srsearch=brain&format=json")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/more")
def wikipedia_links():

    def striptags(text):
        return Markup(text).striptags()

    wiki_items = requests.get(WIKI_URI).json()
    items = [(item['title'], striptags(item['snippet'])) for item in wiki_items['query']['search']]
    return render_template("more.html", pages=items)


@app.route("/scramble", methods=['POST'])
def scramble():
    text = request.form["text"]
    return render_template("scrambled.html", text=textScrambler.scramble(text))
