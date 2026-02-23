#this program ask for language input then get the result
def greeting(lang):
	if lang =="es":
		print("Halo")
	elif lang == "fr":
		print("bonjour")
	else :
		print("Hello")

lang = input("enter your speakin language!\n")

greeting(lang)

