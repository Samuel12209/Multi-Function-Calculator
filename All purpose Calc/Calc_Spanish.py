import math
print("Calculator")
print("-"*10)

print("¿Qué tipo de matemáticas quieres hacer?")
mathing = int(input("(Suma, Resta, Multiplica, Divide, Exponente, Raíz cuadrada, Terum de Pitágoras, Pi, Cuadrado |(1,2,3,4,5,6,7,8,9):"))

if mathing == 1:
  print("Suma")
  print("-"*10)
  n1 = int(input("primer número: "))
  n2 = int(input("segundo numero: "))
  n3 = n1 + n2
  print("-"*10)
  print(n3)
  print("-"*10)
if mathing == 2:
  print("Resta")
  print("-"*10)
  n1 = int(input("primer número: "))
  n2 = int(input("segundo numero: "))
  n3 = n1 - n2
  print("-"*10)
  print(n3)
  print("-"*10)
if mathing == 3:
  print("Multiplica")
  print("-"*10)
  n1 = int(input("primer número: "))
  n2 = int(input("segundo numero: "))
  n3 = n1 * n2
  print("-"*10)
  print(n3)
  print("-"*10)

if mathing == 4:
  print("Divide")
  print("-"*10)
  n1 = int(input("primer número: "))
  n2 = int(input("segundo numero: "))
  n3 = n1 / n2
  print("-"*10)
  print(n3)
  print("-"*10)


if mathing == 5:
  print("Exponente")
  print("-"*10)
  n1 = int(input("exponent: "))
  n2 = int(input("Nuber: " ))
  n3 = n1 ** n2
  print("-"*10)
  print(n3)
  print("-"*10)

if mathing == 6:
  print("Raíz cuadrada")
  print("-"*10)
  n1 = int(input("numero: ") )
  n3 = math.sqrt(n1)
  print("-"*10)
  print(n3)
  print("-"*10)

if mathing == 7:
    print("Terum de Pitágoras")
    print("-"*10)
    typep = input("¿Qué estás resolviendo?: ").lower()
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
    math_type = input("Radio, Circo, area: ").lower()
    print(math_type)
    if math_type == "radio":
      print("-"*10)
      area = int(input("area: "))
      radius = math.sqrt(area / math.pi)
      print(radius)
      print("-"*10)
    if math_type =="circo":
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
  print("Cuadrado")
  print("-"*10)
  mathtype = input("Area, Perimetro: ").lower()
  if mathtype == "area":
    print("Area")
    n1 = int(input("Side: "))
    n2 = int(input("Side: "))
    n3 = n1 * n2
    print(n3)
  if mathtype =="perimetro":
    print("Perimiter")
    n1 = int(input("Side1: "))
    n2 = int(input("Side2: "))
    n3 = n1 * 2 + n2 * 2
    print(n3)

print("Gracias por usando!")
yesno = input("¿finalizado?(Enter To Escape)")