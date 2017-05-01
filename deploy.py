from flask import Flask, render_template
import jinja2

app = Flask(__name__)

@app.route('/',methods=["GET"])
def index():
	return render_template('mapage.html')
	#return '<H1>Et Voila !!!</H1>'

if __name__ == "__main__":
	app.run(debug=True)