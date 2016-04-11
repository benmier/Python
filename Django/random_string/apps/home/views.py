from django.shortcuts import render,redirect
import random,string

def index(request):
	try:
		request.session['attempt']
	except:
		request.session['attempt']=0;
		request.session['randomWord']=''
	context = {
		'attempt': request.session['attempt'],
		'randomWord': request.session['randomWord'],
	}
	return render(request, 'home/index.html', context)

def generate(request):
	request.session['attempt']+=1
	request.session['randomWord'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(14))
	return redirect('/')
