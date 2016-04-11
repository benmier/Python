from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth import forms

class Index(View):
	form = forms.UserCreationForm
	form2 = forms.AuthenticationForm
	def get(self,request):
		context = {
			'form':self.form,
			'form2':self.form2,
		}
		return render(request, 'home/index.html', context)
	
	def post(self,request):
		form = self.form(request.POST or None)
		form2 = self.form(request.POST or None)
		if form.is_valid():
			form.save()
			return HttpResponse("Registered")
		else:
			return render(request, 'home/index.html', {'form':form})

class Login(Index):
	def post(self,request):
		form = self.form(None,request.POST)
		print "*"*50
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
		if user is not None:
			login(request,user)
			return HttpResponse("Logged In")