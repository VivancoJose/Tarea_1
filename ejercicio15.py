#EJERCICIO 15.- Crea una aplicación que permita adivinar un número. En primer lugar la aplicación solicita
#  un número entero por teclado. A continuación va pidiendo números y va respondiendo si el número  a adivinar
#  es mayor o menor que el introducido. El programa termina cuando se acierta el número.

print ( "--------------------Ejercicio_15------------------")
numero_secreto = int(input (" numero secreto: \n"))
numero = int (input("numero:"))
while numero != numero_secreto:
    if numero > numero_secreto:
        print("el numero a encontrar es menor del que ingreso")
    else:
        print("el numero a encontrar es mayor del que ingreso")
    numero = int(input("Numero:"))
print("Has acertado el numero ")