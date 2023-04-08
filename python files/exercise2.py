#LOOP FOR IN RANGE

#             start, end, step
for sum in range(1, 11, 1):
    print(sum)
    


for i in range(10):
  previous = i-1
  
  # if para asignar 0
  if previous <= -1: previous = 0
  
  sum = previous + i

  print(sum)
  
  
  

# OTRA MANERA
  
print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

# loop from 1 to 10
for i in range(0, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    # modify previous number
    # set it to the current number
    previous_num = i  # SE LE VA ASIGNANDO EL VALOR DE i EN CADA ITERACIÓN