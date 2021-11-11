#1.	Elabore un programa en Python que imprima los 100 primeros numeros
# naturales. Emplee listas y bucle while

contador=0
list_numeros=[]
while contador <= 100:
  list_numeros.append(contador)
  contador+=1
print(list_numeros)