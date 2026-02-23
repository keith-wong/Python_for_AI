def greet(lang):
	if lang== "es":
		return"Hola"
	elif lang == "fr":
		return "bonjour"
	else:
		return "hello"

lang = input("enter your specking language!\n")

print (greet(lang), "John")
print (greet(lang), "Sally")
print (greet(lang), "Candy")

