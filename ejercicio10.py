#EJERCICIO 10.- Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “passwd#” se indica “Has entrado al sistema”, sino se da un error.

print ( "--------------------Ejercicio_10------------------")

nombre = str(input (" Ingrese el nombre de usuario : \n"))
print(nombre)
if nombre == str("pepe"):
      print("usuario logeado")
else:
    print ("usuario incorrecto")
 

contraseña = str(input (" Ingrese la contraseña : \n"))
print(contraseña)
if  contraseña ==  "passwd#" :
    print("Has entrado al sistema")
else: 
    print("Error, contraseña incorrecta")

    
