from django.shortcuts import render,redirect

def index(request):
	try:
		request.session['count']
	except:
		request.session['count']=0
	return render(request, 'surveys/index.html')

def process(request):
	request.session['name'] = request.POST['name']
	request.session['dojo'] = request.POST['dojo']
	request.session['lang'] = request.POST['lang']
	request.session['comment'] = request.POST['comment']
	request.session['count']+=1
	return redirect('/result')

def show(request):
	context = {
		'name': request.session['name'],
		'dojo': request.session['dojo'],
		'lang': request.session['lang'],
		'comment': request.session['comment'],
		'count': request.session['count'],
	}
	return render(request, 'surveys/process.html', context)

