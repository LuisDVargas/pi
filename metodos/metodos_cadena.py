cadena1 = "Hola maquina soy Dalto"
cadena2 = "37"
cadena3 = "Luis,Daniel,Vargas,Sanchez"

#convierte a mayuscula
mayus = cadena1.upper()

#convierte a minusculas
minus = cadena1.lower()

#primer letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coencidencias devuelve -1
busqueda_find = cadena1.find("D")

#buscamos una cadena en otra cadena, si no hay coencidencias lanza una excepcion
buqueda_index = cadena1.index("D")

#si es numerico, devolvemos true , inno devolvemos false
es_numerico = cadena2.isnumeric()

#si es alfanumerico devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()

#contamos las coincidencias de una cadena, dentro de otra cadena, delvuelve la cantidad de coencidencias
contar_coincidencias = cadena1.count("a")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#veificamos si una cadena empieza con una cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("Ho")

#veificamos si una cadena termina con una cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("o")

#remplaza un pedazo de la cadena
cadena_nueva = cadena1.replace("Hola","Holu maquina")
cadena_nueva1 = cadena3.replace(","," ")
cadena_nueva_1 = cadena_nueva1.capitalize()

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena3.split(",")

print(cadena_separada[0])