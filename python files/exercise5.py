# Program that compares if the first number of a list is equal to the last number of it

def first_last(numbers):
  
  number_i = numbers[0]
  number_f = numbers[len(numbers) - 1]
  
  if number_i == number_f:
    return True
  else:
    return False

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print("result is" + " " + str(first_last(numbers_x)))  # Output: True
print("result is" + " " + str(first_last(numbers_y)))  # Output: False
