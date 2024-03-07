import math
print("Calculator")
print("-"*10)


mathing = int(input("What type of math do you want to do? (Add, Subtract, Multiply, Divide, Exponent, Square root, Pythagorean therum, Pi, Square, Tax |(1,2,3,4,5,6,7,8,9,10): "))

if mathing == 1:
  print("Adding")
  print("-"*10)
  n1 = int(input("First number: "))
  n2 = int(input("Second number: "))
  n3 = n1 + n2
  print("-"*10)
  print(n3)
  print("-"*10)
if mathing == 2:
  print("Subtracting")
  print("-"*10)
  n1 = int(input("First number: "))
  n2 = int(input("Second number: "))
  n3 = n1 - n2
  print("-"*10)
  print(n3)
  print("-"*10)
if mathing == 3:
  print("Multiplying")
  print("-"*10)
  n1 = int(input("First number: "))
  n2 = int(input("Second number: "))
  n3 = n1 * n2
  print("-"*10)
  print(n3)
  print("-"*10)

if mathing == 4:
  print("Dividing")
  print("-"*10)
  n1 = int(input("First number: "))
  n2 = int(input("Second number: "))
  n3 = n1 / n2
  print("-"*10)
  print(n3)
  print("-"*10)


if mathing == 5:
  print("Exponents")
  print("-"*10)
  n1 = int(input("exponent: "))
  n2 = int(input("Nuber: " ))
  n3 = n1 ** n2
  print("-"*10)
  print(n3)
  print("-"*10)

if mathing == 6:
  print("Square Roots")
  print("-"*10)
  n1 = int(input("Number: ") )
  n3 = math.sqrt(n1)
  print("-"*10)
  print(n3)
  print("-"*10)

if mathing == 7:
    print("Pythagorean Therum")
    print("-"*10)
    typep = input("What are you solving for?: ").lower()
    if typep =="c":
        a = int(input("A: "))
        b = int(input("B: "))
        c = math.hypot(a,b)
        print("-"*10)
        print(c)
        print("-"*10)
    if typep =="a":
        c = int(input("C: "))
        b = int(input("B: "))
        a = math.sqrt(c ** 2 - b ** 2)
        print("-"*10)
        print(a)
        print("-"*10)
    if typep =="b":
        a = int(input("A: "))
        c = int(input("C: "))
        b = math.sqrt(c ** 2 - a ** 2)
        print("-"*10)
        print(b)
        print("-"*10)

if mathing == 8:
    print("Pi")
    print("-"*10)
    math_type = input("Radius, Circ, Area: ").lower()
    print(math_type)
    if math_type == "radius":
      print("-"*10)
      area = int(input("Area: "))
      radius = math.sqrt(area / math.pi)
      print(radius)
      print("-"*10)
    if math_type =="circ":
      print("-"*10)
      radius = int(input("Radius: "))
      circumference = 2 * math.pi * radius
      print(circumference)
      print("-"*10)

    if math_type =="area":
      print("-"*10)
      radius = int(input("Radius: "))
      area = math.pi * radius ** 2
      print(area)
      print("-"*10)
if mathing == 9:
  print("sqaure")
  print("-"*10)
  mathtype = input("Area, Perimiter: ").lower()
  if mathtype == "area":
    print("Area")
    n1 = int(input("Side: "))
    n2 = int(input("Side: "))
    n3 = n1 * n2
    print(n3)
  if mathtype =="perimiter":
    print("Perimiter")
    n1 = int(input("Side1: "))
    n2 = int(input("Side2: "))
    n3 = n1 * 2 + n2 * 2
    print(n3)
  
if mathing == 10:
  print("Tax")
  print("-"*10)
  amount =int(input("How much household income do you have: "))
  tax = str(round(amount/10.725))
  print("you owe: " + tax + " Dollars")
  print("-"*10)

print("Thanks for using!")
yesno = input("Finsished?(Enter To Escape)")