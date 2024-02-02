def bolas():
    import math

    def input_ball(n):
        return float(input(n))

    def input_coordinates_radius():
        x = input_ball("Coordenada x del centro: ")
        y = input_ball("Coordenada y del centro: ")
        r = input_ball("Radio de la bola: ")
        return x, y, r

    def ball_collide():
        print("Ingrese las coordenadas de la primera bola:")
        x1, y1, r1 = input_coordinates_radius()

        print("Ingrese las coordenadas de la segunda bola:")
        x2, y2, r2 = input_coordinates_radius()
        
            #formula investigada
                #la fórmula calcula la distancia euclidiana entre dos puntos en un plano 2D,
                #que es la longitud de la línea recta que une esos dos puntos. Esto es útil, por ejemplo,
                #para determinar si dos bolas (u objetos en general) están lo suficientemente cerca para colisionar. 
                #Si la distancia entre los centros es menor o igual a la suma de los radios, entonces hay una colisión.
        
                
                #se resta la cordenada x2 - la cordenada x-1 y se saca la potenciacion luego se hace lo mismo con y2-y1 y estos dos resultados se suman
                #y al resultado final se le calcular la raíz cuadrada con la función math.sqrt() 
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        rad = r1 + r2

        print("--------------------------------")
        print("¿Las dos bolas ingresadas chocan?")
        return distancia <= rad

    # Ejemplo de uso
    print(ball_collide())

#---------------------------------------------------------------------------------------------------------_#
    
def diccionario(panaderia):
    # Almacena los productos con su respectivo precio en un diccionario.
    panaderia = {"inventario": ("rosquilla", "cascarita", "churros", "pan de queso"),
                "Precios": (3000, 1000, 2500, 2000)
                }

    # Muestra el menú
    print("Bienvenido a la panaderia :3")
    print("Menu actual:")
    print(panaderia)

    # Pide datos de compra y cantidad
    p = str(input("Ingrese lo que desea comprar de la lista anterior: "))
    c = int(input("Ingrese la cantidad que desea de este producto: "))

    # Comprueba si el caracter ingresado se encuentra en el diccionario de inventario
    if p in panaderia["inventario"]:
        # .index se usa para obtener la posición del producto p en la lista de inventario.
        # y lo almacena en la variable index
        index = panaderia["inventario"].index(p)
        # Según el index anterior, halla la ubicación del precio de este producto.
        precio = panaderia["Precios"][index]
        print(f"Producto: {p}\n Precio: {precio*c}\n Cantidad: {c}")
    else:
        print(f"{p} no está en el inventario.")

    ## Desarrollado por Eduar Damian Chanaga GOnzalez - 1095581647

    ## Desarrollado por Eduar Damian Chanaga GOnzalez - 1095581647
#---------------------------------------------------------------------------------------------------------_#
        
def findingbugs():
    #-----Correcto-------------------------------------------Incorrecto-----#
    def negate(num):                                    #def negate(num):
        return -num                                         #return -num
    def large_num(num):                                 #def large_num(num):
        return num > 10000                                  #res = (num > 100000)

    b = 9000                                            #negate(b)
    neg_b = negate(b)                                   #neg_b = num
    print("b:", b, "neg_b:", neg_b)                     #print "b:", b, "neg_b:",neg_b

    big = large_num(b)                                  #big = large_num(b)
    print("b in big:", big)                             #print "b in big:",big


    #1. Definir un valor para b
    #2. Llamar a la función negate con el valor de b y asignar el resultado a neg_b
    #3. Llamar a la función large_num con el valor de b y asignar el resultado a big

    ## Desarrollado por Eduar Damian Chanaga GOnzalez - 1095581647

#---------------------------------------------------------------------------------------------------------_#
def mutability(): 
    #-----------------------#
    #-Mutables e inmutables-#
    #-----------------------#
    print("\033[1;91m Mutable")
    print("\033[90mPuede cambiar después de creación")
    print("1. Lista")
    print("2. Diccionario")

    # Mutable (Cambiable)
    # 1. Lista
    lista_mutable = [1, 2, 3]
    print("\033[1;97mLista original:", lista_mutable)
    lista_mutable[0] = 10  # Modificar la lista
    print("Lista modificada:", lista_mutable)

    # 2. Diccionario
    diccionario_mutable = {'a': 1, 'b': 2, 'c': 3}
    print("Diccionario original:", diccionario_mutable)
    diccionario_mutable['a'] = 100  # Actualizar valor en el diccionario
    print("Diccionario modificado:", diccionario_mutable)
    #///////////////////////////////////////////////////////////////////
    # Inmutable (No cambiable)
    # 1. Cadena
    print("\033[91m Inmutable")
    print("\033[90mNo puede cambiar después creación.")
    print("1. Cadena")
    print("2. Tupla")
    cadena_inmutable = "Hola"
    print("\033[1;97mCadena original:", cadena_inmutable)
    # Intentar modificar la cadena generará un error
    # cadena_inmut[0] = 'X'  # Esto lanzará un TypeError

    # 2. Tupla
    tupla_inmutable = (1, 2, 3)
    print("Tupla original:", tupla_inmutable)
    # Intentar modificar la tupla generará un error
    # tupla_inmut[0] = 10  # Esto lanzará un TypeError

    ## Desarrollado por Eduar Damian Chanaga GOnzalez - 1095581647    
#---------------------------------------------------------------------------------------------------------_#
def listas():

        #----------- Lista [] list()--------------
        #Las listas se pueden modificar
    listao = list(["eduar", "damian", "chanaga", "gonzalez","yolanda"])
    print(listao) #Devuelve la lista completa
    print(len(listao)) #Cant de objetos en una lista, en este caso 4
    print(listao[4]) #Devuelve el valor alojado en la posición 1 (yolanda)
    listao[3] = "Modificar" #Esto SI Es valido en el código

    #--------------- Tupla() tuple() --------------------
    #Las tuplas no se pueden modificar, se quedan tal y como estan para siempre
    Tupla = tuple(("1", "2", "3"))
    print(Tupla)

    #--------------- Diccionario{"Key" : "Value",} Dict() --------------------
    Diccionario = {
        "Nombre": "eduar",
        "Edad": "16",
        "Apellido": "chanaga"
    }
    print(Diccionario) #Devuelve todo lo alojado en el dict
    print(Diccionario.get("Nombre")) # .get devuelve el valor que esta en clave
    print(Diccionario.keys()) #Devuelve todas las claves del dict

    #--------------- Conjuntos{} -------------------
    #parecidos a las tuplas, no se accede a los elementos por su índice y tampoco almacena datos duplicados
    conjunto =  {"eduar","eduarchanaga", 16, "petro", "eduarchanaga"}
    print(conjunto) # {16, 'eduarchanaga', 'petro', 'eduar'} El elemento eduarchanaga al estar repetido solo se pone una vez
    #print(conjunto[3]) --> No puede acceder al elemento de su índice

    ## Desarrollado por Eduar Damian Chanaga GOnzalez - 1095581647