class bike(object):
	def __init__(self,price,max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print "Price: $",self.price
		print "Max Speed: ",self.max_speed
		print "Miles: ",self.miles
		print "---------------------------"
		return self
	def ride(self):
		print "Riding"
		self.miles+=10
		return self
	def reverse(self):
		print "Reversing"
		self.miles-=5
		if self.miles<0:
			self.miles=0
		return self

bike1 = bike(200,"25mph")
bike1.ride().ride().ride().reverse().displayInfo()

bike2 = bike(300,"35mph")
bike2.ride().ride().reverse().reverse().displayInfo()

bike3 = bike(400,"150mph")
bike3.reverse().reverse().reverse().displayInfo()