diccionario = {
    "nombre" : 'lucas',
    "apellido" : 'dalto',
    "subs" : 1000000
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continua)
valor_de_kasdks = diccionario.get("kasdks")
print("Hola papa el pograma continua")

#elimina todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("subs")

#obteniendo un elemento dirct_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)