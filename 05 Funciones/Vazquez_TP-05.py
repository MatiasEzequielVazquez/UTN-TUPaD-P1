#1
def imprimir_hola_mundo():
    print("Hola Mundo!")
    
imprimir_hola_mundo()    

#2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

#3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#4
from math import pi
def calcular_area_circulo(radio):
    return round((pi * (radio ** 2)), 2)

def calcular_perimetro_circulo(radio):
    return round((2 * pi * radio), 2)

radio = int(input("Ingrese el radio de un circulo: "))
print(f"En base al radio {radio} de un circulo, "
      f"el area es: {calcular_area_circulo(radio)} "
      f"y el perimetro es: {calcular_perimetro_circulo(radio)}")

#5
def segundos_a_horas(segundos):
    horas = segundos // 3600
    resto_horas = segundos % 3600
    minutos = resto_horas // 60
    segundos_restantes = segundos % 60
    return int(horas), int(minutos), int(segundos_restantes)

segundos_total = int(input("Ingrese una cantidad de segundos: "))
h, m, s = segundos_a_horas(segundos_total)
print(f"{h} horas, {m} minutos, {s} segundos")

#6
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} * {i} : {numero * i}")

num = int(input("Ingresa un numero: "))
tabla_multiplicar(num)

#7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
resultado_operaciones = operaciones_basicas(a, b)
print (f"En base a los numeros {a} y {b}, " 
      "para las siguientes operaciones basicas los resultados son: "
      f"\nsuma: {resultado_operaciones[0]}"
      f"\nresta: {resultado_operaciones[1]}"
      f"\nmultiplicacion: {resultado_operaciones[2]}"
      f"\ndivision: {resultado_operaciones[3]}")

#8
def calcular_imc(peso, altura):
    return round((peso / altura ** 2), 2)

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"En base a su peso de {peso}KG y altura de {altura}M, "
      f"su IMC es de: {calcular_imc(peso, altura)}kg/m2")

#9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
celsius = float(input("Ingrese una temperatura en Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit")

#10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3
a, b, c = map(float, input("Ingrese 3 números separados por espacio: ").split())
print(F"El promedio de {a, b, c} es: {calcular_promedio(a, b, c)}")
