#Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.

print ( "--------------------Ejercicio_9------------------")

numero = int(input (" Ingrese un numero : \n"))
print(numero) 
if numero == 0:
    print("el valor no esta permitido")
elif numero > 12:
    print("el valor esta fuera del rango")

if numero == 1:
    print ("El mes correspondinete es Enero y tiene 31 dias")
elif numero == 2:
    print ("El mes correspondinete es Febrero y tiene 28 dias")
elif numero == 3:
    print ("El mes correspondinete es Marzo y tiene 31 dias")
elif numero == 4:
    print ("El mes correspondinete es Abril y tiene 30 dias")
elif numero == 5:
    print ("El mes correspondinete es Mayo y tiene 31 dias")
elif numero == 6:
    print ("El mes correspondinete es Junio y tiene 30 dias")
elif numero == 7:
    print ("El mes correspondinete es Julio y tiene 31 dias")
elif numero == 8:
    print ("El mes correspondinete es Agosto y tiene 31 dias")
elif numero == 9:
    print ("El mes correspondinete es Septiembre y tiene 30 dias")
elif numero == 10:
    print ("El mes correspondinete es Octubre y tiene 31 dias")
elif numero == 11:
    print ("El mes correspondinete es Noviembre y tiene 30 dias")
elif numero == 12:
    print ("El mes correspondinete es Dicieimbre y tiene 31 dias")

print ("fin del programa")
   

