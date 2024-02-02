##-----------------------
##-----Ejercicio 1-------
##-----------------------

##Impresion en consola
print ("Hola mundo")
# ---- Datos primitivos ----
#1. String
texto = "campus"
print(texto)
print(type(texto))
#2. int
numeroentero= 1
print(numeroentero)
print(type(numeroentero))
#3. float
numerodecimal=1.1
print(numerodecimal)
print(type(numerodecimal))

#4. double
numerodecimallargo =3.14123534523412314564524223123123
print(numerodecimallargo)
print(type(numerodecimallargo))
#5. Boolean
booleano = True
print(booleano)
print(type(booleano))
#----- Entradas por parte del usuario con definicion de tipo de dato primitivo ----

Entradausuario = str(input("Ingresa tu nombre -> "))
print (f"Tu nombre es: {Entradausuario} ")


EntradausuarioNumero = int(input("Ingresa tu edad -> "))
print (f"Tu edad es: {EntradausuarioNumero} ")
#---- Siclos ----
#ciclo for
for i in range (5,10,2):
    print(i)
#ciclo white
booleanito=True
while booleanito == True:#while condicion_a_cumplir :
    print("Sigo vivo")
    booleanito=False

#---- COndicionales ----
text1="campus"
if text1 == "campus":
    print("Soy campus")
else:
    print("No soy campus")
## Desarrollado por Eduar Damian Chanaga GOnzalez - 1095581647