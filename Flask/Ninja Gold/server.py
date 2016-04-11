from flask import Flask, render_template, request, redirect, session, flash
from random import randint
from datetime import datetime
app = Flask(__name__)
app.secret_key = "thisisasecret"

@app.route('/')
def index():
	try:
		session['yourGold']
	except:
		session['yourGold'] = 0
		session['message'] = []
	return render_template("index.html", yourGold=session['yourGold'], arr=session['message'])

@app.route('/process_monkey', methods=['POST'])
def input():
	if  request.form['building']=='farm':
		reward = randint(10,20)
		session['yourGold']+=reward
		session['message'].append("Earned "+str(reward)+" golds from the farm! ("+str(datetime.now())+")") 
		return redirect('/')
	elif request.form['building']=='cave':
		reward = randint(5,10)
		session['yourGold']+=reward
		session['message'].append("Earned "+str(reward)+" golds from the cave! ("+str(datetime.now())+")")
		return redirect('/')
	elif request.form['building']=='house':
		reward = randint(2,5)
		session['yourGold']+=reward
		session['message'].append("Earned "+str(reward)+" golds from the house! ("+str(datetime.now())+")") 
		return redirect('/')
	elif request.form['building']=='casino':
		reward = randint(-50,50)
		session['yourGold']+=reward
		if reward>=0:
			session['message'].append("Earned "+str(reward)+" golds from the casino! ("+str(datetime.now())+")") 
		else:
			session['message'].append("Lost "+str(abs(reward))+" golds from the casino! ("+str(datetime.now())+")") 
	return redirect('/')
app.run(debug=True)