list1 = [101, 32, 88, 74, 66]

for num in list1:
	print(num)
		

		
def create_list(length):
	list = []
	for i in range(length):
		print("Enter the", i + 1, "number: ")
		number = int(input())
		list.append(number)
	
	return list
	
list_size = int(input("Size of your list: "))
print("Your new list is:", create_list(list_size))


# x = input("Ingresa lo que sea")
# print(type(x)) # input always is str type
# you must specify the type enclosing it


