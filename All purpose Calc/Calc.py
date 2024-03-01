from collections.abc import Sequence
import math
print("Calculator")
print("-"*10)

mathing = int(input("What type of math do you want to do? (add, subtract, multiply, divide, exponent, square root,Pythagorean therum(1,2,3,4,5,6,7) "))

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

if mathing == 7:
    print("Pythagorean Therum")
    print("-"*10)
    typep = input("What are you solving for?: ")
    if typep =="C":
        a = int(input("A: "))
        b = int(input("B: "))
        c = math.hypot(a,b)
        print("-"*10)
        print(c)