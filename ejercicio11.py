#Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.

print ( "--------------------Ejercicio_11------------------")

año = int(input (" Ingrese un año : \n"))
print(año)

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print (f"El año {año},es un año bisiesto")
        else: 
             print (f"El año {año},  ingresado no es bisiesto")
    else: 
        print (f"El año {año},es un año bisiesto")
else:
    print(f"El año {año},  ingresado no es bisiesto")