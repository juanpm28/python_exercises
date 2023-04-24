# Program that takes odd numbers from the first list and even numbers from the second list and makes a new list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

list1_new = []
list2_new = []

for num in list1:  # iterates one element in the list per loop
  if num % 2 != 0:
    list1_new.append(num)

for num in list2:
  if num % 2 == 0:
    list2_new.append(num)

list3 = list1_new + list2_new
print(list3)

# Another way of doing the problem with range

# for i in range(len(list1)):
#   if list1[i] % 2 != 0:
#     list1_new = list1_new + [list1[i]]

# for i in range(len(list2)):
#   if list2[i] % 2 == 0:
#     list2_new = list2_new + [list2[i]]
