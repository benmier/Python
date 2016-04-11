from random import randint
import datetime

test = []
for i in range(0,1000):
	test.append(randint(0,10000))
# print test

startTime = datetime.datetime.now()
endTime = datetime.datetime.now()
x = True
n = len(test)-1
while x==True:
	temp = False
	for i in range(0,n):
		if test[i]>test[i+1]:
			test[i+1],test[i] = test[i],test[i+1]
			temp = True
	if not temp:
		x = False
		endTime = datetime.datetime.now()
print "Microseconds per Number: ",((endTime.microsecond-startTime.microsecond))/1000