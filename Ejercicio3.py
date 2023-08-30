#TALLER 3 PYTHON
# AUTORIA: JOHANA VANESSA MOSQUERA OLAYA
# FECHA: 21/AGOSTO/2023


from datetime import date
hoy = date.today()
print("Hoy es el dia: ", hoy)

a= int(input("Digite el valor de A: "))
b= int(input("Digite el valor de B: "))
if a>=b:
    print("A es igual o mayor que B")
else :
    print("A es menor que B")
print ()

curso1="Requerimientos"
curso2="algoritmos"
print("El curso 1 es: ", curso1)
print("El curso 2 es: ", curso2)
if curso1 == "Requerimientos" and curso2 == "algoritmos":
    print("Usted estudia programacion de Software")
else:
    print("Usted estudia otro Programa diferente a programacion de software")
    print()
    print("***Final del Analisis del programa de FOrmacion SENA ***")
    print()
frase= input("Digite una oracion: ")
print("La frase en mayuscula es: ", frase.upper())
longitud= len(frase)
print("La longuitud de la frase  es: " ,len(frase) , "caracteres")
if longitud>10:
    print("La frase contine mas de 10 caracteres")
else:
    print("La frase contiene menos de 11 caracteres")
    print()
    print("FIN")
print()
# CODIGO MODIFICADO

nombre= input("Ingrese su nombre ")
apellio= input("Ingrese su apellido ")
edad= int(input("Ingrese su edad "))

if edad>18:
    print("Usted es mayor de edad ")
else:
    print("Usted no cuenta con la edad suficiente")
    print()
celular= input("Ingrese su numero de celular ")
cantidad= len(celular)
if  cantidad >= 10:
    print()
else:
    print("Datos erroneos")
terminos = input("Si acepta los termonos y condiciones escriba si de lo contrario escriba no ")
if terminos == "si":
          print("Bienvenido a nuestro portal web")
else:
    print("Lo sentimos no cuentas con los requisitos para acceder al portal web")
