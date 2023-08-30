#TALLER 6 PYTHON
#AUTORA: JOHANA VANESSA MOSQUERA  ><
#FECHA: 30/AGOSTO/2023

from datetime import date
hoy = date.today()
print ("Hoy es el dia: ", hoy)
print()
print("TALLER 6 CICLO ITERABLES CON LA SENTENCIA WHILE")
print()
num1=int(input("digite un numero: "))
print("***Cilco controlador por controlador")
i= 1
while i <= num1:
    print(i)
    i+=1
print('fin ciclo')
print()
print("***Cilco controlador por evento")
i= 1
numero1=5
numero2=int(input("digite un numero del 1 al 10: "))


while numero2 != numero1:
    print(i)
    i+=1
    numero2=int(input("digite un numero del 1 al 10: "))
print("Acertaste en el intento No.", i)
print('fin ciclo')
print()
print("***Cilco abordado con la sentencia break")
amistad=input("digite nombre de una amistad: ")
amistad= amistad.upper()

for charter in amistad:
    print(charter)
    if charter=="A":
        break
print("fin del ciclo")
print()
print("FIN")
