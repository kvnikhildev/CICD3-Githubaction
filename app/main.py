"""Main Flask app module."""

from flask import Flask,jsonify 

app = Flask(__name__)

@app.route('/')
def home():
    """Return a greeting."""
    return jsonify({"message": "Hello, world!"}) 
