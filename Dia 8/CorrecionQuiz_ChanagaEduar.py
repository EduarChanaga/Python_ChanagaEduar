def calcular_definitiva(lista):
    # Multiplicar cada nota por su respectivo porcentaje
    lista[0] *= 0.3  # La nota 1 representa el 30%
    lista[1] *= 0.3  # La nota 2 representa el 30%
    lista[2] *= 0.4  # La nota 3 representa el 40%
    # Calcular la suma de las notas ya multiplicadas por su porcentaje
    sumatoria = sum(lista)
    return sumatoria

for i in range(5):
    print("Estudiante#", i+1)
    lista = []
    notaMayor = 0
    definitiva = 0
    for j in range(3):
        numerito = float(input("Ingresa tu nota: "))
        print(numerito)
        definitiva += numerito
        if numerito > notaMayor:
            notaMayor = numerito
        lista.append(numerito)
    print(lista)
    # Llamar a la función para calcular la nota definitiva
    definitiva = calcular_definitiva(lista)
    print("Tu definitiva es:", definitiva)
    if definitiva < 2:
        print("Perdiste tu vida.")
    elif definitiva < 3:
        print("Pues... todo bien... recupera")
    elif definitiva > 4.5:
        print("¡Excelente estudiante! Eres ejemplar")
    print(lista)
