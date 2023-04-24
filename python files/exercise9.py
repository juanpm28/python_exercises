# Program that checks if a number is a palindrome 
# 121 is a palindrome number because if reversed it stays the same

number = int(input("Enter a number: "))
reversed_number = 0
original_num = number  # This is needed because the number variable gets affected forever because of the while loop

while number != 0:
  remainder = number % 10 # To get the last digit of the number
  reversed_number = (reversed_number * 10) + remainder # Multiply * 10 necessary to add the digit 
  number //= 10 # To delete the last digit 

if original_num == reversed_number:
  print("Yes, the number is a palindrome")
else:
  print("The number is not a palindrome")