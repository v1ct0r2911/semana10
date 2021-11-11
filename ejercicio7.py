#7.Considere que tiene registrado en una tupla el sueldo de 5 empleados,
# obtener el sueldo más alto y más bajo.
sueldos=(500,200,350,1000)
menor=0
mayor=0
for sueldo in sueldos:
    if mayor < sueldo:
       mayor=sueldo

    if menor>sueldo:
       menor=sueldo
print(menor)
print(mayor)