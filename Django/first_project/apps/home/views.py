from django.shortcuts import render

def index(request):
	context = {
		'name': 'Ben',
		'sport': 'baseball',
		'lang': 'Python',
	}
	return render(request, 'home/index.html', context)
