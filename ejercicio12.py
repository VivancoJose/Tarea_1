# Programa que lea un carácter por teclado y compruebe si es una letra mayúscula.

print ( "--------------------Ejercicio_12------------------")

caracter = str(input (" Ingrese un caracter para determinar si es mayuscula o no : \n"))
print(caracter)
if caracter == "a"<= caracter <="z":
    print ("El caracter ingresado es una letra minuscula")
if caracter == "A"<= caracter <="Z":
     print ("El caracter ingresado es una letra mayuscula")