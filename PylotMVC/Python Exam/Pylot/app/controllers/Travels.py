from system.core.controller import *
from datetime import datetime

class Travels(Controller):
	def __init__(self, action):
		super(Travels, self).__init__(action)
		self.load_model('Travel')
		self.load_model('User')

	def dashboard(self):
		trips = self.models['Travel'].all_trips()
		return self.load_view('/show/dashboard.html', trips=trips)

	def add_page(self):
		print "#"*50
		print datetime.date(datetime.now())
		return self.load_view('/new/add.html')

	def add(self):
		trip = {
			'destination':request.form['destination'],
			'description':request.form['description'],
			'start_date':request.form['start_date'],
			'end_date':request.form['end_date'],
		}
		new_trip = self.models['Travel'].add_trip(trip)
		if new_trip!=False:
			return redirect('/travels')
		else:
			return redirect('/travels/add')

	def destination(self,id):
		trip = self.models['Travel'].trip_by_id(id)
		users = self.models['Travel'].users_by_trip_id(id)
		return self.load_view('/show/destination.html', trip=trip, users=users)

	def join(self,id):
		self.models['Travel'].join_trip(id)
		return redirect('/travels')

