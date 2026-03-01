sentence = "mary had a little lamp" #define our string variable
count = 0  #define our counter

for index in sentence : # define iteration variable index
	if index == "a" : # when letter 'a' is cound update the counter by 1
		count = count +1
print (f"total number of letter 'a' is {count}")




