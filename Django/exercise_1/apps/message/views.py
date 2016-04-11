from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View

class MyView(View):
	def get(self,request):
		return render(request, 'message/index.html')

	def post(self,request):
		return HttpResponse('Message submitted')
