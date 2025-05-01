# ----------------------------------------------
# 1 Add a color to the list of colors
# ----------------------------------------------
def add_color(color):

  if color not in colors_list: 
    colors_list.insert(0, color)
    print (f"Color {color.upper()} added to list...")
  else:
    print (f"Color {color.upper()} already exists in list...") 


colors_list = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']

color = "brown"
# color = "red"

#  add_color(color)

# for color in colors_list:
#   print (color)

# print ("-" * 40)

# ----------------------------------------------
# 2 Calculadora
# ----------------------------------------------
def calculator (num1, num2, oper):
  match oper:
    case 1: return num1 + num2
    case 2: return num1 - num2
    case 3: return num1 * num2
    case 4: 
      if num2 != 0:
        return num1 / num2
      else:
        return 0
    case 5: 
      if num2 != 0:
        return num1 % num2
      else:
        return 0
    case 6: return num1 ** num2


oper_str = ["mas", "menos", "por", "entre", "modulo de", "elevado a"]
oper_str = ["+", "-", "*", "/", "mod", "^"]
resp = "s"

while True:

  num1 = num2 = oper = result = 0

  print ("\nCALCULADORA")
  print ("1-Sumar")
  print ("2-Restar")
  print ("3-Multiplicar")
  print ("4-Dividir")
  print ("5-Modulo")
  print ("6-Exponente")
  print ("7-Todas")
  print ("8-Salir")

  oper = int(input("Operacion: "))

  if (oper == 8):
    print ("Adios!")
    break

  if oper not in range(1, 9):
    print ("Operacion invalida, intente nuevamente...")
    break

  num1 = float(input(f"Numero 1: "))
  num2 = float(input(f"Numero 2: "))

  if oper != 7:

    result = round(calculator (num1, num2, oper), 2)

    print (f"{num1} [ {oper_str[int(oper)-1]} ] {num2} = {result}")

  else:
    for i in range(1, 7):
      result = round(calculator (num1, num2, i), 2)
      print (f"{num1} [ {oper_str[i-1]} ] {num2} = {result}")

  # resp = input("\n¿Desea continuar?: ")