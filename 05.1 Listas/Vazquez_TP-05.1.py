#1
miLista = list(range(0, 101, 4))
print(miLista[:])

#2
miLista = ["manzanas", 2, True, [1, False, "Naranja"]]
print(miLista[-1])

#3
lista_vacia = []
miLista = ["elem1", "elem2", "elem3"]

for i in miLista:
    lista_vacia.append(i)

print(lista_vacia)

#4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales[:])

#5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

""" 
Define una lista con 5 items.
La funcion max() identifica el numero maximo en base a un parametro, en este caso la lista numeros.
La funcion remove() permite remover un item de la lista en base al valor exacto del item (no su indice),
en este caso el remove es sobre lo que devuelve la funcion max().
Imprime en pantalla la lista luego de haber removido el numero maximo.
"""

#6
numeros = list(range(10, 30 + 1, 5))
print(numeros[:2])

#7
autos = ["sedan", "polo", "suran", "gol"]
for i in range(1, 3):
    autos.pop(i)
    if i == 1:
        autos.insert(1,"civic")
    else:
        autos.insert(2, "hilux")
print(autos)

#8
miLista = [5, 10, 15]
dobles = []
for i in miLista[:3]:
    dobles.append(i*2)
print(dobles)

#9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove(compras[0][0])
print(compras)

#10
lista_anidada = []
items = [15, True, 25.5, 57.9, 30.6, False]
for i in range(0, 4):
    if i == 2:
        lista_anidada.append(list(items[2:5]))
    elif i == 3:
        lista_anidada.append(items[-1])
    else:
        lista_anidada.append(items[i])

print(lista_anidada)