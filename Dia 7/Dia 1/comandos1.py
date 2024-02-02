def main(Entradausuario,EntradausuarioNumero):
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

    print (f"Tu nombre es: {Entradausuario} ")
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
        
def parametros (nombre,edad):
    ##--------------------------------------------------
    ##----- Ejercicio1_Sin_Parametro_Sin_Retorno -------
    ##--------------------------------------------------
    def diHola():
        
        
        print(f"Bienvenido {nombre}")

    diHola()  

    ##--------------------------------------------------
    ##----- Ejercicio2_Con_Parametro_Sin_Retorno -------
    ##--------------------------------------------------

    def holaConNombre(edad):
        print(f"edad: {edad}")
    holaConNombre(edad) 

    ##--------------------------------------------------
    ##----- Ejercicio3_sin_Parametro_con_Retorno -------
    ##--------------------------------------------------

    def multi():
        print("multiplicacion de dos numeros")
        n1 = float(input("Ingrese el primer numero ---> "))
        n2 = float(input("Ingrese el segundo numero ---> "))
        return n1 * n2

    result = multi()
    print(result)

    ##--------------------------------------------------
    ##----- Ejercicio4_con_Parametro_con_Retorno -------
    ##--------------------------------------------------

    def suma(a,b):
        return a + b 
    print("suma de dos numeros")
    n1=float(input("Ingrese el primer numero ---> "))
    n2=float(input("Ingrese el segundo numero ---> "))
    result = suma(n1,n2)
    print(result)


    ##--------------------------------------------------
    ##------------------- Arreglos ---------------------
    ##--------------------------------------------------

    n_Elementos = int(input("Cuantos nombres quiere almacenar: "))
    lista = []

    for i in range(n_Elementos):
        elemento = str(input(f"Ingrese el nombre {i + 1}: "))
        lista.append(elemento)
    ##Ejemplo de crear lista con bucles
        

    # Imprimir la lista y la suma
    print("Lista ingresada:", lista)

    ## Desarrollado por Eduar Damian Chanaga GOnzalez - 1095581647



