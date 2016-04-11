from django.shortcuts import render
from .models import User,Interest

def index(request):
	return render(request, 'interests/index.html')

def all(request):
	users = User.objects.all().select_related('interest')
	context = {
		'users':users,
	}
	return render(request, 'interests/all.html', context)

def one(request, user_id):
	user = User.objects.filter(id=user_id).select_related('interest')
	context = {
		'user':user,
	}
	return render(request, 'interests/one.html', context)

