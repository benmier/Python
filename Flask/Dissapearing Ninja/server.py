from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def show_user_profile():
    return render_template("ninja.html")

@app.route('/ninja/<color>')
def color(color):
    return render_template("color.html", color=color)
app.run(debug=True)