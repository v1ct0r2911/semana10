#2.	Elabore un programa en Python que registre en una tupla los 
# nombres de los 12 meses, luego deberá ingresar un número que corresponda 
# al mes e imprimir el nombre del mes.Es decir, si ingresa 1 deberá imprimir 
# Enero, si ingresa 2 deberá imprimir Febrero y asi sucesivamente. El programa
# finalizará cuando ingrese un número negativo o cero.
months=(
    "enero",
    "febrero",
    "marzo",
    "abril",
    "mayo",
    "junio",
    "julio",
    "agosto",
    "setiembre",
    "octubre",
    "nobiembre",
    "diciembre"
)
while True:
  numero=int(input("numero del mes: "))
  if numero<= 0:
      print("el numero tiene que ser mayo que 0")
      break
  print(months[numero-1])