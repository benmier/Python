from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "thisisasecret"

@app.route('/')
def index():
	session['count'] += 1
	return render_template("index.html")

app.run(debug=True)