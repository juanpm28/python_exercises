# number1 = 10
# number2 = 15

# sum = number1 + number2

# print("The result is", sum)  # se añade espacio por default

# num1 = int(input("Ingresa el primer numero: "))  # Para ingresar SOLO enteros
# num2 = int(input("Ingresa un segundo numero: "))

# print("La suma de los números es:", num1 + num2)

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

mult = numero1 * numero2

suma = numero1 + numero2

if mult <= 1000:
  print("La multiplicación es:", mult)
else:
  print("La suma es:", suma)


# THE SAME AS ABOVE BUT WITH A FUNCTION
  def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1 + num2

# first condition
result = multiplication_or_sum(20, 30)
print("The result is", result)

# Second condition
result = multiplication_or_sum(40, 30)
print("The result is", result)