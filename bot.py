#!/usr/bin/env python3


import os
from flask import Flask

app = Flask(__name__)

@app.route("/test")
def hello():
    return "Hello world!"

app.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
