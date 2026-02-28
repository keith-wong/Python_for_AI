# this program search for a value in a list

found = False # define boolean variable found to be False

print("Before finding", found )

for item in [9, 41, 12, 3, 74, 14]:
	if item == 3:
		found = True
		print(found, item)
		break        # if value 3 is found we break out the loop
	print (found, item)
#	break    #break outt the loop  if item is found 

print ("After searching we found the item ", item)



 


