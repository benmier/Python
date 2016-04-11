class car(object):
	def __init__(self,price,speed,fuel,milage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.milage = milage
		if price>10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.display_all()
	def display_all(self):
		print "\nPrice:",self.price
		print "Speed:",self.speed
		print "Fuel:",self.fuel
		print "Milage:",self.milage
		print "Tax:",self.tax
		return self

car1 = car(2000,"35mph","Full","15mpg")
car2 = car(2000,"5mph","Not Full","105mpg")
car3 = car(2000,"15mph","Kinda Full","95mpg")
car4 = car(2000,"25mph","Full","25mpg")
car5 = car(20000000,"45mph","Empty","25mpg")