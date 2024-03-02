from collections.abc import Sequence
import math
print("Calculator")
print("-"*10)

mathing = int(input("What type of math do you want to do? (Add, Subtract, Multiply, Divide, Exponent, Square root, Pythagorean therum, PI(1,2,3,4,5,6,7,8):  "))

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
        print("-"*10)
    if typep =="A":
        c = int(input("C: "))
        b = int(input("B: "))
        a = math.sqrt(c ** 2 - b ** 2)
        print("-"*10)
        print(a)
        print("-"*10)
    if typep =="B":
        a = int(input("A: "))
        c = int(input("C: "))
        b = math.sqrt(c ** 2 - a ** 2)
        print("-"*10)
        print(b)
        print("-"*10)

if typep == "8":
  print("PI")
  typep1 = input("Radius, Circumference, area")
print("Thanks for using!")