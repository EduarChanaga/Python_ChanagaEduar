#-----------------------#
#-Mutables e inmutables-#
#-----------------------#
print("\033[1;91m Mutable")
print("\033[90mPuede cambiar después de creación")
print("1. Lista")
print("2. Diccionario")

# Mutable (Cambiable)
# 1. Lista
lista_mutable = [1, 2, 3]
print("\033[1;97mLista original:", lista_mutable)
lista_mutable[0] = 10  # Modificar la lista
print("Lista modificada:", lista_mutable)

# 2. Diccionario
diccionario_mutable = {'a': 1, 'b': 2, 'c': 3}
print("Diccionario original:", diccionario_mutable)
diccionario_mutable['a'] = 100  # Actualizar valor en el diccionario
print("Diccionario modificado:", diccionario_mutable)
#///////////////////////////////////////////////////////////////////
# Inmutable (No cambiable)
# 1. Cadena
print("\033[91m Inmutable")
print("\033[90mNo puede cambiar después creación.")
print("1. Cadena")
print("2. Tupla")
cadena_inmutable = "Hola"
print("\033[1;97mCadena original:", cadena_inmutable)
# Intentar modificar la cadena generará un error
# cadena_inmut[0] = 'X'  # Esto lanzará un TypeError

# 2. Tupla
tupla_inmutable = (1, 2, 3)
print("Tupla original:", tupla_inmutable)
# Intentar modificar la tupla generará un error
# tupla_inmut[0] = 10  # Esto lanzará un TypeError

## Desarrollado por Eduar Damian Chanaga GOnzalez - 1095581647