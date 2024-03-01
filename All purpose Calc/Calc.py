from collections.abc import Sequence
import math
print("Calculator")
print("-"*10)

mathing = int(input("What type of math do you want to do? (add, subtract, multiply, divide, exponent, square root(1,2,3,4,5,6) "))

if mathing == 1:
  print("Adding")
  print("-"*10)
  n1 = int(input("First number: "))
  n2 = int(input("Second number: "))
  n3 = n1 + n2
  print("-"*10)
  print(n3)

if mathing == 2:
  print("Subtracting")
  print("-"*10)
  n1 = int(input("First number: "))
  n2 = int(input("Second number: "))
  n3 = n1 - n2
  print("-"*10)
  print(n3)

if mathing == 3:
  print("Multiplying")
  print("-"*10)
  n1 = int(input("First number: "))
  n2 = int(input("Second number: "))
  n3 = n1 * n2
  print("-"*10)
  print(n3)


if mathing == 4:
  print("Dividing")
  print("-"*10)
  n1 = int(input("First number: "))
  n2 = int(input("Second number: "))
  n3 = n1 / n2
  print("-"*10)
  print(n3)



if mathing == 5:
  print("Exponents")
  print("-"*10)
  n1 = int(input("exponent: "))
  n2 = int(input("Nuber: " ))
  n3 = n1 ** n2
  print("-"*10)
  print(n3)


if mathing == 6:
  print("Square Roots")
  print("-"*10)
  n1 = int(input("Number: ") )
  n3 = math.sqrt(n1)
  print(n3)