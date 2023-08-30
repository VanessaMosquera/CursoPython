# TALLER 1 CURSO PYTHON
# AUTOR: VANESSA MOSQUERA
# FECHA: 14/08/2023

from datetime import date
hoy = date.today()
print ("Hoy es el dia:" , hoy)

print("Ejercicio con tipo de dato Entero ")
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
suma = n1 + n2
resta = n1- n2
producto = n1*n2
division= n1/n2

print("La suma es = ", suma)
print("La resta es = ", resta)
print("La multiplicación es = ", producto)
print("La división es = ", division)
print(" ")

# CODIGO MODIFICADO
print("Ejercicio con tipo de dato Float ")

numero= float(input("Ingrese un numero: "))
numeroDos= float(input("Ingrese otro numero: "))
resultSuma = numero + numeroDos
resultResta = numero- numeroDos
resultMultiplicacion = numero*numeroDos
resultDivision= numero/numeroDos
 
print("La suma es = ", resultSuma)
print("La resta es = ", resultResta)
print("La multiplicación es = ", resultMultiplicacion)
print("La división es = ", resultDivision)

print("FIN")


