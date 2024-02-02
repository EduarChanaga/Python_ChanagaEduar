
    #----------- Lista [] list()--------------
    #Las listas se pueden modificar
listao = list(["eduar", "damian", "chanaga", "gonzalez","yolanda"])
print(listao) #Devuelve la lista completa
print(len(listao)) #Cant de objetos en una lista, en este caso 4
print(listao[4]) #Devuelve el valor alojado en la posición 1 (yolanda)
listao[3] = "Modificar" #Esto SI Es valido en el código

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
conjunto =  {"eduar","eduarchanaga", 16, "petro", "eduarchanaga"}
print(conjunto) # {16, 'eduarchanaga', 'petro', 'eduar'} El elemento eduarchanaga al estar repetido solo se pone una vez
#print(conjunto[3]) --> No puede acceder al elemento de su índice

## Desarrollado por Eduar Damian Chanaga GOnzalez - 1095581647