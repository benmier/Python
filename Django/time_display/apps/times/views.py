from django.shortcuts import render
from time import strftime

def index(request):
	date = strftime('%B %d, %Y')
	time = strftime('%H:%M %p')
	context = {
		'date': date,
		'time': time,
	}
	return render(request, 'times/index.html', context)
