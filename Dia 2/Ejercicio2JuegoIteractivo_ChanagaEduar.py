##-----------------------
##---- Ejercicio 2 ------
##--- N° Aleatorio ------
##-----------------------
import random #se importa la funcion random para poder generar un numero aleatorio
decision=str("si")

#Imprime la informacion para que el usuario tenga claro el funcionamiento del programa
print("\x1b[1;33m-> Bienvenido <-")
print("El programa generara un numero aleatorio entre 1 y 100 y tu deber sera adivinarlo.")
print("con el paso de los intentos se te iran dando pistas para que logres el resultado.")
print("Tendra 10 intentos maximos para hallar el resultado.")
print("-----------")

print("-> Comencemos <-")
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
   