#creando una lista (se puede modificar)
lista = ["lucas Dalto", "Soy dalto", True,1.85]

#creando una tupla (no se puede modificar)
tupla = ("lucas Dalto", "Soy dalto", True,1.85)

#modificando la lista y comentando el codigo
#tupla[3]="maquimola"
#lista[3]= "maquinola"

#imprimiendo las lista y tupla tomando el elmento numero 3
#print(lista[3])
#print(tupla[3])

#creando un conjunto set (no se accede a elementos por indice, noo almacena daros duplicados)
conjunto = {"lucas Dalto", "Soy dalto", True,1.85,"Soy dalto"}

#print(conjunto) -> mp puede acceder al elemento

#creando un diicionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : "lucas dalto",
    'anal' : "soy dalto",
    'esta_emocionado' : True,
    'altura' : 1.85,
    'dato_duplicado' : "soy dalto"
}

print(diccionario['altura'])
print(lista[3])
