#6.	Considere que tiene registrado en una tupla la edad de 8 amigos.
# El programa deberá solicitar la edad a buscar e imprimir el número 
# de amigos que tienen dicha edad.
edades=[3,6,9,9,12,15,15,15,18,21]
while True:
 numeros=int(input("introduce edad:"))
 print(edades.count(numeros)) 
