# this program is to find the average in a list of numbers

count = 0  # create a counter 
sum = 0     # create variable sum
print ("Before average : ", count, sum)

for value in [9, 41, 12, 3, 74, 15]:
	count =  count + 1
	sum = sum + value
	print (count,sum, value)

x = round (sum / count, 2)
 

print (f"after average of {count} items, total of {sum}, average is {x}")



