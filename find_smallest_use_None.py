smallest = None

print ("Before comparison!")

for value in [9, 14, 12, 3, 74, 15]:
	if smallest is None:
		smallest = value
	elif value < smallest:
		smallest = value
	print (smallest, value)

print ("after comparison" , smallest)


