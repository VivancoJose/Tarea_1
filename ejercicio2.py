#EJERCICIO 2.- Calcular el perímetro y área de un círculo dado su radio

print("-----------------------ejercicio_2--------------------------")

import math

radio = int (input (" Ingrese el radio del circulo : \n"))
print(radio)

#perimetro de un circulo: 2 pi * r    

perimetro = 2 * math.pi * radio
print ("EL perimetro es igual a: \n" , perimetro)

#Area de un circulo: pi * r ^ 2  

area = math.pi * radio**2
print ("EL area es igual a: \n" , area)



 





