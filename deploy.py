from flask import flask

app = Flask(__name__)
@app.route('/')
def index():
	return '<h1>Deploye ds Heroku</h1>'