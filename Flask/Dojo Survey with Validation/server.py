from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "thisisasecret"

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/result', methods=['POST'])
def input():
	name = request.form['name']
	comment = request.form['comment']
	dojo = request.form['dojo']
	lang = request.form['lang']
	if len(request.form['comment'])>1:
		flash("Comment cannot be more than 120 characters!")
		return redirect('/')
	elif len(name)>120:
		flash("Name cannot be blank!")
		return redirect('/')
	else:
		return render_template("result.html", name=name, lang=lang, dojo=dojo, comment=comment)
app.run(debug=True)