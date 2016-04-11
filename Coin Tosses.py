heads = 0
tails = 0
from random import randint
for i in range(1,5001):
	if randint(0,1)==0:
		tails+=1
		print "Attempt #",i,": Throwing a coin... It's a tail!... Got ",heads," head(s) so far and ",tails," tail(s so far)"
	else:
		heads+=1
		print "Attempt #",i,": Throwing a coin... It's a head!... Got ",heads," head(s) so far and ",tails," tail(s) so far"