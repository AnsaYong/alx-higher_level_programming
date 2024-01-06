#!/usr/bin/python3
""" Web server
"""
from flask import Flask
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
    """ Root
    """
    return "my index page"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
    
