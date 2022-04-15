from flask import Flask, jsonify, render_template
from jinja2 import Template
import requests

app = Flask(__name__, template_folder='templates')

jsonData = {'name': 'Aaron',
            'email': 'aaron@mail.com',
            'password': '123abc'}

t = Template("Hello{{ token }}")


@app.route('/')
def home():
    return 'welcome'


@app.route('/json', methods=['GET', 'POST'])
def json():
    return jsonify(jsonData)


@app.route('/jinja/<username>')
def jinja(username):
    return render_template('index.html', username=username)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
