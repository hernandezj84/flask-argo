"""App module"""
import copy
import flask
from flask import Flask, jsonify, request, make_response, Response
from flask_cors import CORS
import requests
from src.config import OK_STATUS, BAD_REQUEST

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/test")
def test():
    """Test method to check if everything is working well

    Returns:
        [type]: [description]
    """
    return make_response(jsonify({"TEST": "OK"}), )

@app.route("/test/post", methods=(['POST']))
def test_post():
    """_summary_
    """
    request_data = request.json
    return make_response(jsonify(request_data), OK_STATUS)
