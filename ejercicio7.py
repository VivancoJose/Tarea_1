    #EJERCICIO 7.- Realiza un programa que pida dos números ‘a’ y ‘b’ e indique si su suma es positiva, negativa o cero.
print ( "--------------------Ejercicio_7------------------")

valor_1 = int(input (" Ingrese un valor para el primer numero : \n"))
print(valor_1)

valor_2 = int(input (" Ingrese un valor para el segundo numero : \n"))
print(valor_2)

suma = valor_1 + valor_2

if suma > 0:
    print  ("La suma de los valores ingresados es positiva")
elif suma < 0:
    print ("La suma de los valores ingresados es negativa")
else:  
    print ("La suma de los valores ingresados es nula")