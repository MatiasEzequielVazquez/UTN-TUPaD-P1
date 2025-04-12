#1 
for i in range (0, 101):
    print(i)

#2
num = int(input("Ingresa un numero entero: "))
contador = 1
while True:
    if num < 10:
        break
    contador += 1
    num = num / 10
print(contador)

#3
num1 = int(input("Ingresa un numero entero: "))
num2 = int(input("Ingresa otro numero entero: "))
suma = 0
for i in range (num1, num2 + 1):
    suma = suma + i
print(suma)

#4
num = int(input("Ingresa 0 para salir\nO ingrese un numero a sumar: "))
suma = 0
while num != 0:
    suma = suma + num
    print(f"\nEl resultado actual de la suma es: {suma}\n")
    num = int(input("Ingresa 0 para salir\nO ingrese otro numero a sumar: "))

#5
from random import randint
aleatorio = randint(0, 9)
print("Se ha generado un numero aleatorio")
num = int(input("Adivina cual es el numero: "))
contador = 1
while True:
    if num == aleatorio:
        print(f"Haz acertado en {contador} intentos, el numero era {aleatorio}")
        break
    else:
        contador += 1
        print ("Ese no es el numero..., intenta otra vez.")
        num = int(input("Adivina cual es el numero: "))


#6
for i in range (100, 0, -1):
    if i % 2 == 0:
        print(i)

#7
num = int(input("Ingresa un numero: "))
suma = 0
for i in range (0, num + 1):
    suma = suma + i
print(suma)

#8
pares = 0
impares = 0
positivos = 0
negativos = 0
contador = 1

while contador <= 100:  
    num = int(input("Ingrese un numero: "))
    if num < 0: 
        negativos += 1
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    else:
        positivos += 1
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    contador += 1
    
print(f"\nDe los numeros ingresados:\n"
      f"{pares} fueron pares\n"
      f"{impares} fueron impares\n"
      f"{positivos} fueron positivos\n"
      f"{negativos} fueron negativos")

#9
from statistics import mean
lista = []
contador = 1
while contador <= 100:  
    num = int(input("Ingrese un numero entero: "))
    lista.append(num)
    contador += 1
media = mean(lista)
print ("La media es: ", media)

#10
num = int(input("Ingrese un numero: "))
lista = list(str(num))
lista_inversa = []
for i in reversed(lista):
    lista_inversa.append(i)
lista_inversa = int(''.join(lista_inversa))
print(lista_inversa)