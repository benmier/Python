from random import randint
import datetime

test = []
for i in range(0,100):
	test.append(randint(0,10000))
print test

endTime = datetime.datetime.now()
new = []
startTime = datetime.datetime.now()
while len(test)>0:
	min = test[-1]
	for i in range(0,len(test)-1):
		if test[i]<min:
			min=test[i]
	test.pop(test.index(min))
	new.append(min)
endTime = datetime.datetime.now()
print new
print "Microseconds per Number: ",((endTime.microsecond-startTime.microsecond))/1000