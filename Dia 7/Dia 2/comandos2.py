def fibonacci():
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
                elif n==0:
                    break
                else:
                    print("Por favor, ingrese un número entero mayor que 0.")
                
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

                #Try ejecuta una serie de codigo y si se detecta un error no va a cerrar el programa,
                #al encontrar un error se ejecutara el except valueError

        if n==0:
            break
        elif n > 1:
            print("Termino 1: 0")
            print("Termino 2: 1")    
        elif n == 1:  
            print("Termino 1: 0")
            
    
        for i in range(1, n-1):
            fibonacci_secuencia = fibonacci(i)
            print(f"Término {i+2}: {fibonacci_secuencia[-1]}")
        print("--------------------------------------------------------------------------------------------------------------------")
        ###Decision de repetir 
        print("Desea repetir?")
        Decision=input("---> ")
    ## Desarrollado por Eduar Damian Chanaga GOnzalez - 1095581647
def juegoiteractivo():
    ##-----------------------
    ##---- Ejercicio 2 ------
    ##--- N° Aleatorio ------
    ##-----------------------
    import random #se importa la funcion random para poder generar un numero aleatorio
    decision=str("si")

    #Imprime la informacion para que el usuario tenga claro el funcionamiento del programa


    print("x1b[1;33m-> Comencemos <-")
    while (decision=="Si" or decision=="si"):
        numero_aleatorio = random.randint(1, 100)  #genera numero aleatorio
        
        while True:
            for i in range(0, 10):
                while True:
                    try:
                        numero_aleatorio2=int(input(f"\x1b[1;33m (intento {i+1}) Ingrese un numero --> "))
                        if numero_aleatorio2 > 0:
                            break  #Sirve para que en un (while True) se ejecute hasta llegar a esta linea de codigo
                        else:
                            print("\033[4;35m Por favor, ingrese un número entero mayor que 0.")
                    except ValueError:
                        print("\033[4;35m Por favor, ingrese un número entero válido.")

                if(numero_aleatorio==numero_aleatorio2): #Si el numero ingresado es = al aleatorio imprime una felicitacion y finaliza el while
                    print(f"\033[94m Felicidades, el numero {numero_aleatorio2} es el correcto")
                    print(f"\033[94m Total de intentos: {i+1}")
                    i==10
                    break
                ##Comprueba si es mayor o menor y imprime la respectiva pista
                elif(numero_aleatorio2>numero_aleatorio):
                    print(f"El numero secreto es menor a {numero_aleatorio2} ")
                elif(numero_aleatorio2<numero_aleatorio):
                    print(f"El numero secreto es mayor a {numero_aleatorio2}")
                    
                elif(i==10):
                    break

                else:
                    print("")
            break
        #repetir while inicial o finalizar
        print("\033[4;37m Desea volver jugar? (Si-No)")
        decision=input("--> ")    
    ##Desarrollado por Eduar Damian Chanaga GOnzalez - 1095581647
    