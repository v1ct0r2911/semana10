#3.	Realice un programa en Python que registre en una lista 
# la tabla de multiplicar de un número ingresado por teclado  
# e imprima la lista
lista=[]
t=0
i=0
n=int(input("ingrese numero"))
while i < 12:
    i+=1
    t+=n
    lista.append(t)
print(lista)