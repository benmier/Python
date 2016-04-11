a = [1, 2, 5, 10, 255, 3]
print sum(a)/len(a)

#Or by using for:
sum = 0
len = 0
for i in a:
	sum+=i
	len+=1
print sum/len