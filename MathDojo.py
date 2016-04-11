class MathDojo(object):
	def __init__(self):
		self.numb = 0
	def add(self,*args):
		for arg in args:
			if type(arg)==list or type(arg)==tuple:
				for i in arg:
					self.numb += i
			else:
				self.numb += arg
		return self
	def subtract(self,*args):
		for arg in args:
			if type(arg)==list or type(arg)==tuple:
				for i in arg:
					self.numb -= i
			else:
				self.numb -= arg
		return self
	def result(self):
		print self.numb

MathDojo().add([1],3,4).add([3,5,7,8],[2,4.3,1.25]).subtract(2,[2,3],[1.1,2.3]).result()
