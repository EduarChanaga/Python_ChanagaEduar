##-----------------------
##---- Exercise 1 -------
##------- coins ---------
##-----------------------

def coins(amount): 
    i = 0
    coins_10 = amount // 10 ##calcula la cantidad de monedas de 10
    print("10:", coins_10)
    amount %= 10 #$Saca el sobrante del paso anterior
    coins_5 = amount // 5
    print("5:", coins_5) ##calcula la cantidad de monedas de 5.
    amount %= 5 #Saca el sobrante al paso anterior.
    coins_1 = amount
    print("1:", coins_1) #Todo lo sobrante lo convierte en monedas de 1.
    print("coins =", coins_1 + coins_5 + coins_10)
    count = []
            ###Contar y agregar a una lista la cantidad de monedas.
    for i in range(coins_10):
        count.append("10")
    for i in range(coins_5):
        count.append("5")
    for i in range(coins_1):
        count.append("1")

    print(count)

while True:
    try: #Comprobar que el numero este entre el rango 1-1000 y que no tenga decimales.
        amount = int(input("--> "))
        if amount > 0 and amount<1000 :
            break  
        else:
            print("Please enter a number greater than 0 and less than 1001.")
    except ValueError:
        print("Please enter a valid integer.")
coins(amount)


## Desarrollado por Eduar Damian Chanaga GOnzalez - 1095581647