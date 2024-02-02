import comandos1
print("Que tarea desea ver")
print("1. main")
print("2. TareaParametrosRetorno")
des=int(input("--> "))

if des == 1:
    comandos1.main()
    print(comandos1.main ())
elif des == 2:
    comandos1.parametros()
    print(comandos1.parametros ())
else:
    print("Tarea no registrada")

    
    

