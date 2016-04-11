from django.shortcuts import render,redirect
from .models import Product
from datetime import datetime

def show(request):
	products = Product.objects.all()
	context = {
		'products':products
	}
	return render(request, 'products/index.html', context)

def edit(request,product_id):
	product = Product.objects.get(id=product_id)
	context = {
		'product':product
	}
	return render(request, 'products/edit.html', context) 

def delete(request,product_id):
	Product.objects.get(id=product_id).delete()
	return redirect('/products')

def update(request,product_id):
	Product.objects.filter(id=product_id).update(manufacturer=request.POST['manufacturer'],name=request.POST['name'],price=request.POST['price'])
	return redirect('/products')

def add(request):
	Product.objects.create(manufacturer=request.POST['manufacturer'],name=request.POST['name'],price=request.POST['price'],date_added=datetime.date(datetime.now()))
	return redirect('/products')