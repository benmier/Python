from django.shortcuts import render

def index(request,ninja_color):
	context = {
		'ninja_color': ninja_color,
	}
	return render(request, 'ninja/index.html', context)
