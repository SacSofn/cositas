print("hola","github",sep=" o.O ")
nombre = input("ingrese su nombre para continuar")
while not nombre.isalpha():
  print("ingrese un nombre valido")
  nombre = input("ingrese su nombre para continuar")

print("ahora su nombre sera puesto alrevez")
for x in reversed(nombre):
  print(x)
