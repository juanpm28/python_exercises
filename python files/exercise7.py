# Program that counts how many times Emma is written in a sentence

x_string = "Emma is a good programmer. Emma always knows what to do. Emma. E. Emma. Em"

number_emmas = x_string.count("Emma")
print("Emma appeared", number_emmas, "times") 

# option 2 with loops and if's

#def emma_count(sentence):
#	number_of_emmas = 0
#	for i in range(len(sentence)):
#		if sentence[i] == "E":
#			i += 1  # i++ not valid in python
#			if sentence[i] == "m":
#				i += 1
#				if sentence[i] == "m":
#					i += 1
#					if sentence[i] == "a":
#						number_of_emmas += 1
#					
#	return number_of_emmas
#	
#print(emma_count(x_string))



