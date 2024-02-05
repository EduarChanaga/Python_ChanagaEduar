import comandos6
while True:
    print("\033[97m--------------")
    print("Que tarea desea ver")
    print("1. Colision de bolas")
    print("2. Diccionario ")
    print("3. FindingBugs ")
    print("4. Mutability ")
    print("5. listas ")
    des=int(input("--> "))
    print("--------------")

    if des == 1:
        print(comandos6.bolas ())
    elif des == 2:
        panaderia = {"inventario": ("rosquilla", "cascarita", "churros", "pan de queso"),
                "Precios": (3000, 1000, 2500, 2000)
                }
        print(comandos6.diccionario (panaderia))
    elif des == 3:
        print(comandos6.findingbugs ())
    elif des == 4:
        print(comandos6.mutability ())
    elif des == 5:
        
        print(comandos6.listas ())
    else:
        print("Tarea no registrada")