##-----------------------
##---- Ejercicio 1 ------
##----- Fibonacci -------
##-----------------------
def fibonacci(n):
    fib_secuencia = [0, 1]

    for i in range(0, n):
        fib_secuencia.append(fib_secuencia[-1] + fib_secuencia[-2])

    return fib_secuencia
Decision=str("si")
print("")
                                                        ##Descripcion serie fibonacci
print("-----------------------------------------------------> Bienvenido <-----------------------------------------------------")
print("La Secuencia de Fibonacci es una serie matemática en la que cada número es la suma de los dos anteriores (0, 1, 1, 2, 3, 5, 8, 13, ...). ")
print("Características notables incluyen su crecimiento exponencial, la convergencia hacia la proporción áurea /≈1.618/, y su presencia en patrones naturales y artísticos.")
print("La secuencia tiene aplicaciones en diversos campos y destaca por su conexión con la armonía en la naturaleza.")
print("")
                                                    ##Inicio de la impresion serie fibonacci
print("-------------------------------------------------------> Inicio <-------------------------------------------------------")
while (Decision=="si" or Decision == "Si"):
    print("")
    print("Ingrese la cantidad de terminos que quiere ver en la serie fibonacci (en entero)")
    while True:
        try:
            n = int(input("--> "))
            if n > 0:
                break  #Sirve para que en un (while True) se ejecute hasta llegar a esta linea de codigo
            else:
                print("Por favor, ingrese un número entero mayor que 0.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

            #Try ejecuta una serie de codigo y si se detecta un error no va a cerrar el programa,
            #al encontrar un error se ejecutara el except valueError


    print("Termino 1: 0")
    print("Termino 2: 1")
    for i in range(1, n-1):
        fibonacci_secuencia = fibonacci(i)
        print(f"Término {i+2}: {fibonacci_secuencia[-1]}")
    print("--------------------------------------------------------------------------------------------------------------------")
    ###Decision de repetir 
    print("Desea repetir?")
    Decision=input("---> ")
    
## Desarrollado por Eduar Damian Chanaga GOnzalez - 1095581647