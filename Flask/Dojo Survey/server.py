from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "thisisasecret"

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/result', methods=['POST'])
def input():
	name = request.form['name']
	dojo = request.form['dojo']
	lang = request.form['lang']
	comment = request.form['comment']
	return render_template("result.html", name=name, lang=lang, dojo=dojo, comment=comment)
	
app.run(debug=True)