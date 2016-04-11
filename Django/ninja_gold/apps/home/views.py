from django.shortcuts import render,redirect
from random import randint

def index(request):
	try:
		request.session['total']
	except:
		request.session['total'] = 0
		request.session['activity'] = []
	context = {
		'gold': request.session['total'],
		'activity': request.session['activity'],
	}
	return render(request, 'home/index.html', context)

def farm(request):
	reward = randint(10,20)
	request.session['total']+=reward
	request.session['activity'].insert(0,'You earned '+str(reward)+' gold from the farm!')
	return redirect('/')

def cave(request):
	reward = randint(5,10)
	request.session['total']+=reward
	request.session['activity'].insert(0,'You earned '+str(reward)+' gold from the cave!')
	return redirect('/')

def house(request):
	reward = randint(2,5)
	request.session['total']+=reward
	request.session['activity'].insert(0,'You earned '+str(reward)+' gold from the house!')
	return redirect('/')
	
def casino(request):
	reward = randint(-50,50)
	request.session['total']+=reward
	request.session['activity'].insert(0,'You earned '+str(reward)+' gold from the casino!')
	return redirect('/')