from crypt import methods
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

json = {'name': 'Aaron', 'email': 'aaron@mail.com', 'password': '123abc'}


@app.route('/')
def home():
    return 'welcome'


@app.route('/json', methods=['GET', 'POST'])
def json():
    return jsonify(json)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
