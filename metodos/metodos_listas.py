#creando una lista con list()
lista = list(["hola","dalto",34,56,23,True])
lista1 = list([1,3,2,4,5,6])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append("JAJAJAJA")

#agegando en elemento a la lista en un indece especifico
lista.insert(2,"TOMA MAMA")

#agegando varios elementos a la lista
lista.extend([False,2030])

print(len(lista))

#eliminando un elemento de la lista (por indice)
lista.pop(-1) #-1 elimina el ultimo, -2 para elimina el antepenultimo

#removiendo un elemento de la lista por su valor
#lista.remove("23")

#eliminando todos los elementos de la lista
#lista.clear()

#ordena la lista de forma ascendente (si usamos el parametro revers=True lo ordena en revesa)
lista1.sort()

#invirtiendo los elementos de una lista
lista1.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(34)

print(elemento_encontrado)