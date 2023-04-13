# Program that finds numbers divisible by 5 

list1 = [10, 20, 33, 50, 55, 74, 100]

def divisible_by_5(list_numbers):
  new_list = []
  for i in range(len(list_numbers)):  
    
    if list_numbers[i] % 5 == 0:
      new_list.append(list_numbers[i])
  return new_list    

divisible_numbers = divisible_by_5(list1)
print(divisible_numbers)  # Output: [10, 20, 50, 55, 100]


# Notes
# return keyword exits a function and return the value that we tried to find to the calling code
# return keyword is useful if you only need to return a SINGLE value
# If i need to return a list in a function, I need to make an empty list to store the values and then print the new list