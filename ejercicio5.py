#EJERCICIO 5.-Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

print("-----------------------ejercicio_5--------------------------")
minutos = int(input (" Ingrese un numero los cuales corresponden a minutos : \n"))
print(minutos)

horas = int (minutos / 60)
m_1 = int (minutos % 60)
print (f"La cantidad ingresada corresponde a {horas}  horas  y {m_1} minutos ")
