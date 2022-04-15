from crypt import methods
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/')
def query_example():
    return 'Query String Example'


@app.route('/form-example')
def form_example():
    return 'Form Data Example'


@app.route('/json', methods=['GET', 'POST'])
def json():

    return jsonify({'name': 'Aaron', 'email': 'aaron@mail.com', 'password': '123abc'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
