class animal(object):
	def __init__(self,name=None):
		self.name = name
		self.health = 100
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		print(self.health)
		return self


ani = animal()
ani.displayHealth().run().run().walk().walk().walk().displayHealth()


class dog(animal):
    def __init__(self):
        self.health = 150
    def pet(self):
        self.health += 5
        return self

dog1 = dog()
dog1.run().run().walk().walk().walk().pet().displayHealth()

class dragon(animal):
    def __init__(self):
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayHealth1(self):
    	print("This is a dragon!")
    	self.displayHealth()

dragon1 = dragon()
dragon1.run().run().walk().walk().walk().fly().fly().displayHealth1()

# ani.fly().displayHealth() <----This doesn't work, as expected
