from flask import Flask, url_for, request


app = Flask(__name__)


@app.errorhandler(400)
def bad_request(e):
    return '<h1>Bad Request!<h1>'


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Hello World!</h1>', 302, [('location', 'https://mi.com')]


@app.route('/hello')
def index():
    return f'<h1>Hello { request.args['name']}!</h1'


@app.cli.command()
def naive():
    """Show 'Hello Naive!'"""
    print('Hello Niave!')

