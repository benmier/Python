from system.core.controller import *

class Products(Controller):
	def __init__(self, action):
		super(Products, self).__init__(action)
		self.load_model('Product')

	def index(self):
		#get request
		#load all products
		products = self.models['Product'].get_all()
		return self.load_view('index.html' products=products)

	def show(self,id):
		#get request
		#find one and render it on view
		product = self.models['Product'].get_one(id)
		return self.load_view('show.html', product=product)

	def edit(self):
		#get request
		#find one and render edit view
		product = self.models['Product'].get_one(id)
		return self.load_view('edit.html', product=product)

	def new(self):
		#get request
		#renders the create page
		return self.load_view('new.html')

	def create(self):
		#post request
		#creates a record in the DB
		create_product = {
			'id':id,
			'name':request.form['name'],
			'description':request.form['description'],
			'price':request.form['price']
		}
		self.models['Product'].create(create_product)
		return redirect('/')

	def update(self,id):
		#post request
		#updates a record in the DB
		create_product = {
			'id':id,
			'name':request.form['name'],
			'description':request.form['description'],
			'price':request.form['price']
		}
		self.models['Product'].update(update_product)
		return redirect('/show/"{}"'.format(id))

	def destroy(self,id): 
		#post request
		#destroys a record in the DB
		self.models['Product'].destroy(id)
		return redirect('/')


