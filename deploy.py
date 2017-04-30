from flask import Flask, render_template, request, jsonify
import jinja2

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('la_page.html')
	#return '<H1>Et Voila !!!</H1>'