#TALLER 4 PYTHON
# AUTORIA: JOHANA VANESSA MOSQUERA OLAYA
# FECHA: 21/AGOSTO/2023


from datetime import date
hoy = date.today() #fecha actual
print("Hoy es el dia: ", hoy)
print()
print("EJERCICIO DE DE LAS CLASES DE TRIANGULO")
a=int(input("Digite el valor de A: "))
b=int(input("Digite el valor de B: "))
c=int(input("Digite el valor de C: "))

if a==b and a==c and b==c:
    print("El triangulo es equilatero")
else:
    if a==b or a==c or b==c:
        print("El triangulo es isoceles")
    else:
        print("El triangulo es escaleno")
print()
animal= input("Digite un animal: ")
animal= animal.upper()

if animal == "PERRO":
    print("Este animal es el mejor amigo del hombre: ", animal)
elif animal == "GATO":
    print("Este animal persigue a los ratones: ", animal)
elif animal == "OSO":
    print("Este animal vive en el polonorte: ", animal)
else:
        print("No es PERRO, no es GATO, ni es OSO es ... : ", animal)
print()
print("FIN")

print()

#CODIGO MODIFICADO

dia=input("ingrese un dia de la semana ")
dia=dia.lower()
if dia == "lunes" or dia == "Martes" or dia == "Mircoles" or dia == "jueves":
    print("El hoario laboral es de 8 a 6")
elif dia == "viernes" or dia == "sabado":
    print("El horario de fin de semana es de 8 a 12")
else:
    print("El dia ingresado no se labora")

print()

estracto= int(input("Ingrese su estracto socioeconomico "))
sisben= int(input("Ingrese su nivel de sisben "))

if estracto >= 0 and sisben <=2:
    print("Tiene derecho a subsidio")
else:
    if estracto >= 3 and sisben <=5:
        print("Tiene derecho a medio subsidio")
    else:
        print("no tiene drecho a subsidio")

