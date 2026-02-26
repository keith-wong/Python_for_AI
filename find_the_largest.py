# set the variable largest_so_far

largest_so_far = -1

print(f"Before : largest so far is {largest_so_far}")

for num in [9, 41,12, 3, 74, 15]:
	if num > largest_so_far:
		largest_so_far = num
		print (largest_so_far, num)
	else:
		print (largest_so_far, num)

print (f"after iteration, largest so far is {largest_so_far}")


