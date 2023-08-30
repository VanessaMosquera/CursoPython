# TALLER DOS PHYTON
# AUTORA: VANESSA MOSQUERA
# FECHA: 14/08/2023

from datetime import date
hoy = date.today()
print("Hoy es el dia: ", hoy)
print(" ")

a=int(input("digite el primer número: "))
b=int(input("digite el primer número: "))
c=int(input("digite el primer número: "))

x=[a,b,c]

print("El valor maximo es: " , max(x))
print("El valor minimo es: ", min(x))
print("La suma de los 3 números es: ", sum(x))
print()


z=float(input("Ingrese un número con decimales: "))
redondo = round(z)
print("el valor de ", z , "redondeado es: " , redondo)
print()

frase = input("Digite una oración: ")
print("La frase en mayusculas es: ", frase.upper())
print("La frase en minusculas es: ", frase.lower())
print("La frase en con mayuscula inicial es: ", frase.capitalize())
print("La frase con palabras en mayusculas es: ", frase.title())
print("La longitud de la frase es: " , len(frase) , "caracteres")
print()
print("FIN")
print()
nombre= input("Ingrese su nombre: ")
ocupacion = input("ingrese su ocupación: ")
junio = float (input("Digite sus ingresos en el mes de Junio: "))
julio = float (input("Digite sus ingresos en el mes de Julio: "))
agosto = float (input("Digite sus ingresos en el mes de Agosto: "))
ingresos = [junio,julio ,agosto]
suma=junio+julio+agosto
suma= round(suma)

print()
print("Su nombre es: ", nombre.upper())
print("Su ocupacion es: ", nombre.capitalize())
print("Sus ingresos maximos fueron de :", max(ingresos), "y sus ingresos minimos fueron de :", min(ingresos))
print("El total de sus ingresos redondeado es de: ", suma)

