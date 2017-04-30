from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Deploye ds Heroku</h1><h3>On y Arrivera !!!</h3>'