#friends = ['joeseph', 'glenn', 'sally']
friends = list()

while True:
	friend = input("enter a friend name: ")
	x = friend
	if x == "done":
		break # check if user input is done , then break
	friends.append(x)
	print(friends)
#	if friend =="done":
#		break
#	print( friends)

for friend in friends:
	print(friend)

print ("piss off")


