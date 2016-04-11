print "Scores and Grades"
score = 0
for i in range(0,10):
	score =  input("Score: ")
	if score<60 or score>100:
		print "Enter a score between 60 and 100" 
	elif score<=69:
		print "Your grade is D"
	elif score<=79:
		print "Your grade is C"
	elif score<=89:
		print "Your grade is B"
	else:
		print "Your grade is A"
	print "End of the program. Bye!"