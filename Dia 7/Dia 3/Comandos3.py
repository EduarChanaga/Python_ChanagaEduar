def coins(amount): 
    i = 0
    coins_10 = amount // 10 ##calcula la cantidad de monedas de 10
    amount %= 10 #$Saca el sobrante del paso anterior
    coins_5 = amount // 5
    amount %= 5 #Saca el sobrante al paso anterior.
    coins_1 = amount
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

