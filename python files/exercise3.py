word = str(input("Write a word: "))

print(len(word))

print("Original string is", word)
print("Printing only even index chars")

for i in range(0, len(word), 2):
  print (word[i])