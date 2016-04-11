from random import randint
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "thisisasecret"

@app.route('/')
def index():
	try:
		session['number']
	except:
		session['number'] = randint(1,10) 
	return render_template("index.html", number=session['number'])

@app.route('/result', methods=['POST'])
def input():
	test = int(request.form['guess'])
	if test<session['number']:
		session['message']="Too Low!"
	elif test>session['number']:
		session['message']="Too High!"
	else:
		session['message']="Correct!"
		session['restart']=1
	return redirect('/')

@app.route('/restart', methods=['POST'])
def restarting():
	session.clear()
	return redirect('/')
	
app.run(debug=True)