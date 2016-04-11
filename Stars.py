def draw_stars(numbs):
	for i in numbs:
		if type(i) == int:
			print "*"*i
		elif type(i) == str:
			print i[0].lower()*len(i)

draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])