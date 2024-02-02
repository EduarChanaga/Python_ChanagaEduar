import comandos2
while True:
    print("--------------")
    print("Que tarea desea ver")
    print("1. Fibonacci")
    print("2. Juego iteractivo")
    des=int(input("--> "))
    print("--------------")

    if des == 1:
        print("-----------------------------------------------------> Bienvenido <-----------------------------------------------------")
        print("La Secuencia de Fibonacci es una serie matemática en la que cada número es la suma de los dos anteriores (0, 1, 1, 2, 3, 5, 8, 13, ...). ")
        print("Características notables incluyen su crecimiento exponencial, la convergencia hacia la proporción áurea /≈1.618/, y su presencia en patrones naturales y artísticos.")
        print("La secuencia tiene aplicaciones en diversos campos y destaca por su conexión con la armonía en la naturaleza.")
        print("")
        print(comandos2.fibonacci ())
    elif des == 2:
        print("\x1b[1;33m-> Bienvenido <-")
        print("El programa generara un numero aleatorio entre 1 y 100 y tu deber sera adivinarlo.")
        print("con el paso de los intentos se te iran dando pistas para que logres el resultado.")
        print("Tendra 10 intentos maximos para hallar el resultado.")
        print("-----------")
        print(comandos2.juegoiteractivo ())
    else:
        print("Tarea no registrada")