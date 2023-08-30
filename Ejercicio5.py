#TALLER 5 PYTHON
#AUTORA: JOHANA VANESSA MOSQUERA
#FECHA: 30/AGOSTO/2023

from datetime import date
hoy = date.today()
print ("Hoy es el dia: ", hoy)
print()
print("TALLER 5CICLOS ITERABLES CON LA SENTENCIA FOR")
print()
num1=int(input("digite el primer número: "))
num2=int(input("digite el segundo número (mayor): "))
print("ciclo para el primer numero")

for i in range(num1):
    print(i)
print('fin del ciclo')

print()
print("ciclo para el primer numero hasta el segundo numero")
for i in range(num1,num2):
    print(i)
print('fin del ciclo')

print()
print("ciclo para el primer numero hasta el segundo numero con incrementos de 2")
for i in range(num1,num2, 2):
    print(i)
print('fin del ciclo')

print()
empresa= input("digite nombre de una empresa: ")
empresa= empresa.lower()
for character in empresa:
    print(character)
    print('fin del ciclo')

print()
print("FIN")


#CODIGO MODIFICADO

print("Ciclo para tabla de multiplicar")
numero = int(input("Digite el número de la tabla a consultar: "))
multiplica = 10

for i in range(1, multiplica + 1):
    resultado = numero * i
    print(numero, "x" , i , "=" , resultado)
print('fin del ciclo')
print()

palabra= input("digite una palabra: ")
palabra2= palabra.lower()
palabra2= palabra2.upper()
for caracter in palabra2:
    print(caracter)
print('fin del ciclo')
print()


palabras=input("digite una palabra : ")
print("ciclo para palbra")
for i in range(len(palabras)):
    print(i)
print('fin del ciclo')
print()
print("FIN")
