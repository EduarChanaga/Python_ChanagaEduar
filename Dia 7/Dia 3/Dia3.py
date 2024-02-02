import Comandos3
while True:
    try: #Comprobar que el numero este entre el rango 1-1000 y que no tenga decimales.
        amount = int(input("--> "))
        if amount > 0 and amount<=1000 :
            break  
        else:
            print("Please enter a number greater than 0 and less than 1001.")
    except ValueError:
        print("Please enter a valid integer.")
print(Comandos3.coins (amount))