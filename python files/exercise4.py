def remove_chars(word, size):
  new_word = word[size:]  # lo que abarca (de size hasta el final) es lo que se mostrará
  return new_word

print(remove_chars("juanadssa", 2))