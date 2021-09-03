#Pedir un número por teclado y mostrar la tabla de multiplicar

print ( "--------------------Ejercicio_13------------------")

numero = int(input (" Ingrese un numero: \n"))
print(numero)
for i in range (0,12):
    resultado = i * numero
    print (("%d * %d = %d")%(numero, i , resultado))