# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.


def exponent(base, exp):
    result = base**exp
    return result
  
base = 2
exp = 5

print(f"{base} raises to the power of {exp}:", exponent(base, exp))
