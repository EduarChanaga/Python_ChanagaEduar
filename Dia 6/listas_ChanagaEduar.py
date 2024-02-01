
    #----------- Lista [] list()--------------
    #Las listas se pueden modificar
listao = list(["eduar", "damian", "chanaga", "gonzalez"])
print(listao) #Devuelve la lista completa
print(len(listao)) #Cant de objetos en una lista, en este caso 4
print(listao[1]) #Devuelve el valor alojado en la posición 1 (Yolanda)
listao[3] = "Modificar" #Esto SI Es valido en el código
3
#--------------- Tupla() tuple() --------------------
#Las tuplas no se pueden modificar, se quedan tal y como estan para siempre
Tupla = tuple(("1", "2", "3"))
print(Tupla)

#--------------- Diccionario{"Key" : "Value",} Dict() --------------------
Diccionario = {
    "Nombre": "eduar",
    "Edad": "16",
    "Apellido": "chanaga"
}
print(Diccionario) #Devuelve todo lo alojado en el dict
print(Diccionario.get("Nombre")) # .get devuelve el valor que esta en clave
print(Diccionario.keys()) #Devuelve todas las claves del dict

#--------------- Conjuntos{} -------------------
#parecidos a las tuplas, no se accede a los elementos por su índice y tampoco almacena datos duplicados
conjunto =  {"eduar","eduarchanaga", 16, "Tutankamon", "eduarchanaga"}
print(conjunto) # {16, 'eduarchanaga', 'Tutankamon', 'eduar'} El elemento juandariver9 al estar repetido solo se pone una vez
#print(conjunto[3]) --> No puede acceder al elemento de su índice