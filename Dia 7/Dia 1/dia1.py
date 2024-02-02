import comandos1
while True:
    print("--------------")
    print("Que tarea desea ver")
    print("1. main")
    print("2. TareaParametrosRetorno")
    des=int(input("--> "))
    print("--------------")

    if des == 1:
        Entradausuario = str(input("Ingresa tu nombre -> "))
        EntradausuarioNumero = int(input("Ingresa tu edad -> "))
        print(comandos1.main (Entradausuario, EntradausuarioNumero))
    elif des == 2:
        nombre=str(input("Ingrese su nombre -> "))
        edad=int(input("Ingrese su edad -> "))
        print(comandos1.parametros (nombre, edad))
    else:
        print("Tarea no registrada")