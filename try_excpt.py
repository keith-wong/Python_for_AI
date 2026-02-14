print("the following code block handle python trace back situation!")
astr = "Hello John Doe"
try:
	istr=int(astr)
except:
	istr="-1"
print(f"first part of the string change from {astr} to integer {istr}")

astr="123"
try:
	istr=int(astr)
except:
	istr="-1"
print(f"second part of the sring change from {astr} to integer {istr}")

