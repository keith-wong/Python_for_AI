sum = 0 #set sum to zero
count = 0 #set counter to zero


while True:
	inp = input("enter a number  :\n" )
#	value = float(inp)
	if inp =="done": 
		break
	value = float(inp)
	sum = sum + value
	count = count + 1

average = sum / count

print ("average", average)

#==============================

num_list=list()
while True:
	inp=input("enter a number :\n")
	if inp == "done":
		break
	value = float(inp)
	num_list.append(value)

average = sum(num_list) / len(num_list)

print("average", average)




