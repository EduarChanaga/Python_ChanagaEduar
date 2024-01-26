##--------------------------------------------------
##----- Ejercicio1_Sin_Parametro_Sin_Retorno -------
##--------------------------------------------------
def diHola():
  print("Hola usuario")
  nombre=str(input("Ingrese su nombre ->"))
  print(f"Bienvenido {nombre}")

diHola()  

##--------------------------------------------------
##----- Ejercicio2_Con_Parametro_Sin_Retorno -------
##--------------------------------------------------

def holaConNombre(edad):
  print(f"edad: {edad}")
edad=int(input("Ingrese su edad -> "))
holaConNombre(edad) 

##--------------------------------------------------
##----- Ejercicio3_sin_Parametro_con_Retorno -------
##--------------------------------------------------

def multi():
    print("multiplicacion de dos numeros")
    n1 = float(input("Ingrese el primer numero ---> "))
    n2 = float(input("Ingrese el segundo numero ---> "))
    return n1 * n2

result = multi()
print(result)

##--------------------------------------------------
##----- Ejercicio4_con_Parametro_con_Retorno -------
##--------------------------------------------------

def suma(a,b):
    return a + b 
print("suma de dos numeros")
n1=float(input("Ingrese el primer numero ---> "))
n2=float(input("Ingrese el segundo numero ---> "))
result = suma(n1,n2)
print(result)


##--------------------------------------------------
##------------------- Arreglos ---------------------
##--------------------------------------------------

n_Elementos = int(input("Cuantos nombres quiere almacenar: "))
lista = []

for i in range(n_Elementos):
    elemento = str(input(f"Ingrese el {i + 1} nombre: "))
    lista.append(elemento)


# Imprimir la lista y la suma
print("Lista ingresada:", lista)

## Desarrollado por Eduar Damian Chanaga GOnzalez - 1095581647