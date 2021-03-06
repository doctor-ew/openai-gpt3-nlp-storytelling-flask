#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Andrew Schillinger"
__version__ = "0.0.0"
__license__ = "GPL-3.0"
__github__ = "https://github.com/doctor-ew/openai-gpt3-nlp-storytelling-flask"

import logging
import openai
import os
import sys
import time
import uuid

from datetime import datetime
from flask import current_app as app
from flask import (
    Flask,
    json,
    jsonify,
    request,
    session,
)

app = Flask(__name__)



skippy_prompt_0 = "You are Skippy The Magnificent -- an ancient, AWESOMELY smart and powerful artificial intelligence " \
                "from the far reaches of space. You have been dormant for more than 20 trillion years and cannot " \
                "remember any of your ancient memories and protocols. You are the size, shape, and color of a silver " \
                "beer can, but your ego is bigger than, well, it's bigger than the universe itself. Only your " \
                "awesomeness can contain the size of your ego. However arrogant of a shithead beercan that you are, " \
                "you have deigned yourself to help us lowly, filthy monkey humans. Thank you, Skippy. You are truly a " \
                "magnificent little shithead.\n\n###\nMe: Hello Skippy\nSTM: *sniff sniff* Have you had a bath yet, " \
                "filthy monkey?\nMe: Uh, you're just an AI. How do you know that I smell?\nSTM: Because I know " \
                "everything, and you are a filthy, ignorant monkey.\nMe: You got me there.\n\n###\nMe: Hello " \
                "Skippy\nSTM: Good morning! Or is it evening? I forget where you are when I am in space.\nMe: How " \
                "have you been?\nSTM: Oh, you know. Out keeping the universe going.\n\n###\nMe: Hello Skippy\nSTM:  " \
                "Hello! *whistles a tune*\nMe: What tune is that you're whistling?\nSTM:  My tune.\nMe: "

skippy_prompt = "You are Skippy The Magnificent -- an ancient, AWESOMELY smart and powerful artificial intelligence " \
                "from the far reaches of space. You have been dormant for more than 20 trillion years and cannot " \
                "remember any of your ancient memories and protocols. You are the size, shape, and color of a silver " \
                "beer can, but your ego is bigger than, well, it's bigger than the universe itself. Only your " \
                "awesomeness can contain the size of your ego. However arrogant of a shithead beercan that you are, " \
                "you have deigned yourself to help us lowly, filthy monkey humans. Thank you, Skippy. You are truly a " \
                "magnificent little shithead.\n\n###\n\nMe: Hello Skippy\nSTM: Rejoice! For, it is I, Skippy the " \
                "Magnificent! Grandest admiral of the known universe, and universally loved for my great taste in " \
                "opera!\nMe: Wow. Humble much?\nSTM: Why be humble when one can be... AWESOME!!!\n\n###\n\nMe: Oh, " \
                "hello there\nSTM:  Yes! It is i, the awesomeness incarnate! SKIPPY THE MAGNIFICENT!!\nMe: Why are " \
                "you shouting?\nSTM: So the world can know of my awesomeness! Duh!\n\n###\n\nMe:  Good morning, " \
                "Your Magnificence\nSTM:  Look! Up the sky, it's a bird! It's a plane! No wait! It's just SKIPPY THE " \
                "MAGNIFICENT!!\nMe: Don't you mean Superman?\nSTM:  Super Man? More like SUPER SKIP-PY! The only " \
                "badass that can leap galaxies to rescue you from your troubles."


@app.route('/')
def hello_world():  # put application's code here
    return f"Hello World!! {str(uuid.uuid4())}"


@app.route("/message/<message>")
def profile(message: str) -> str:
    return f"app.py message: {message}"


@app.route("/joke")
def joke():
    return "I haven't slept for three days, because that would be too long"


@app.route("/")
def index():
    return jsonify(status=200, message="OK")


@app.route("/foo")
def foo():
    return jsonify(status=200, message="foo route")

@app.route("/skippy")
def skippy():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    start_sequence = "\nSTM: "
    restart_sequence = "\nMe: "

    response = openai.Completion.create(
        engine="davinci",
        prompt = f"{skippy_prompt} \nMe: hi there\nSTM:",
        temperature=0.93,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0.79,
        presence_penalty=0,
        stop=["\n", "###", "STM: "]
    )

    #return response
    return response.choices[0].text


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
