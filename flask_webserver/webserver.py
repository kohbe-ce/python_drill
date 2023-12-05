#!/usr/bin/python3

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def default_page():
    return "<h1>Hello, Flask Webserver World!</h1>"


@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello, this is your REST API!'}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)