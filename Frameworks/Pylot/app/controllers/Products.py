from system.core.controller import *

class Products(Controller):
	def __init__(self, action):
		super(Products, self).__init__(action)
		self.load_model('Product')
 
	def index(self):
		#get request
		#load all products
		return self.load_view('index.html')

	def show(self,id):
		#get request
		#find one and render it on view
		return self.load_view('show.html')

	def edit(self):
		#get request
		#find one and render edit view
		return self.load_view('edit.html')

	def new(self):
		#get request
		#renders the create page
		return self.load_view('new.html')

	def create(self):
		#post request
		#creates a record in the DB
		return redirect('/')

	def update(self,id):
		#post request
		#updates a record in the DB
		return redirect('/show/id')

	def destroy(self,id): 
		#post request
		#destroys a record in the DB
		return redirect('/')


