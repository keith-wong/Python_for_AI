# this program find the smallest value in a list

smallest_so_far = 100 # set a large value to compare

print("Before comparison: ", smallest_so_far)

for item in [9, 41, 12, 3, 74, 15]:
	if item < smallest_so_far:
		smallest_so_far = item
		print(smallest_so_far, item)
		break
	print(smallest_so_far, item)

print("after comparison :", smallest_so_far)

  
