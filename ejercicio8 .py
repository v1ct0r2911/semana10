#8.	Se tiene registrado en una tupla los nombres de sus 4 amigos,
# realice un programa en Python que realice una búsqueda por índice 
# e imprimiendo el valor de la tupla correspondiente.
amigos=("dulce", "claudia", "efrain", "cesar")
while  True:
    num=int(input("ingresse un numero del 1 al 4: "))
    if num==0:
        break
    elif num>4:
        print("la posision no existe ")
    else:
        print(amigos[num-1])