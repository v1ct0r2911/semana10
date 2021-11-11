#4.	Realice un programa en Python que registre  n números en una lista hasta 
# que ingrese cero o negativo, luego imprima los valores de la lista de forma 
# de menor a mayor.
numeros=[]
while True:
    numero=int(input("ingrese numeo: "))
    if numero <= 0:
        print("el numero debe ser mayor que 0")
        break
    numeros.append(numero)
print(sorted(numeros))