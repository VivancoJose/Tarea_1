#EJERCICIO 14.-  (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el 
# número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120

print ( "--------------------Ejercicio_14------------------")

numero = int(input (" Ingrese un numero: \n"))
print(numero)
factorial = 1
if numero != 0:
    for i in range (1,numero+1):
        factorial = factorial * i
print ( "el factorial :" , factorial)