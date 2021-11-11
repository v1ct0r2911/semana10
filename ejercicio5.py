#5.	Realice un programa en Python que registre  n números 
# en una lista hasta que ingrese cero o negativo, luego
# imprima los valores de la lista de forma de mayor a menor.
list=[]
num=int(input("ingrese numero: "))
while num > 0:
    list.append(num)
    num=int(input("numero: "))

list.sort()
list.reverse()
print(list)