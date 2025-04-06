# 1
edad = int(input("Ingresa tu edad: "))
if edad > 18:
    print ("Eres mayor de edad")
# 2
nota = int(input("Ingresa tu nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
# 3
num = int(input("Ingresa un numero: "))
while True:
    
    if num % 2 == 0:
        print ("Ha ingresado un numero par")
        break
    else:
        print ("Por favor, ingrese un numero par")
        num = int(input("Ingresa otro numero: "))
# 4
edad = int(input("Ingresa tu edad: "))
if edad < 12:
    print ("Eres un/a Niño/a")
elif edad >= 12 and edad < 18:
    print ("Eres un/a Adolescente")
elif edad >= 18 and edad < 30:
    print ("Eres un/a Adulto/a joven")
else:
    print ("Eres un/a Adulto/a")
# 5
pw = len(input("Ingresa una contraseña: "))
while True:
    
    if pw >= 8 and pw <= 14:
        print ("Ha ingresado una contraseña correcta")
        break
    else:
        print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
        pw = len(input("Ingresa otra contraseña: "))

# 6
from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range (50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print ("Sesgo positivo o a la deracha")
    print (f"La moda es {moda}, la mediana es {mediana} y la media es {media}")
elif media < mediana and mediana < moda:
    print ("Sesgo negativo o a la izquierda")
    print (f"La moda es {moda}, la mediana es {mediana} y la media es {media}")
elif moda == media and media == mediana:
    print ("Sin sesgo")
    print (f"La moda es {moda}, la mediana es {mediana} y la media es {media}")
else:
    print ("Resultado no contemplado")
    print (f"La moda es {moda}, la mediana es {mediana} y la media es {media}")

# 7
frase = str(input("Ingrese una frase o palabra: "))
mi_lista = [frase]
ultimo_char = mi_lista[-1][-1].lower()
vocales = ['a', 'e', 'i', 'o', 'u']
if ultimo_char in vocales:
    print (f"{frase}!")
else:
    print (frase)

# 8
nombre = str(input("Ingrese su nombre: "))
op = int(input("\n1. Si quiere su nombre en mayúsculas" \
               "\n2. Si quiere su nombre en minúsculas" \
                "\n3. Si quiere su nombre con la primera letra mayúscula" \
                 "\n\nElija que opcion desea: "))
if op == 1:
    print(nombre.upper())
elif op == 2:
    print(nombre.lower())
elif op == 3:
    print(nombre.title())
else:
    print("Opcion no valida.")

# 9
magnitud = float(input("Ingrese la magnitud de un terremoto: "))
if magnitud < 3:
    print('"Muy leve" (imperceptible).')
elif magnitud >= 3 and magnitud < 4:
    print('"Leve" (ligeramente perceptible).')
elif magnitud >= 4 and magnitud < 5:
    print('"Moderado" (sentido por personas, pero generalmente no causa daños).')
elif magnitud >= 5 and magnitud < 6:
    print('"Fuerte" (puede causar daños en estructuras débiles).')
elif magnitud >= 6 and magnitud < 7:
    print('"Muy Fuerte" (puede causar daños significativos).')
else:
    print('"Extremo" (puede causar graves daños a gran escala).')

# 10
hemisferio = str(input("Ingrese en que hemisferio se encuentra (N/S): ")).upper()
dia = int(input("Ingrese el dia en que se encuentra (DD): "))
mes = int(input("Ingrese el mes en que se encuentra (MM): "))
if hemisferio == 'N':
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Otoño")
else:
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Primavera")