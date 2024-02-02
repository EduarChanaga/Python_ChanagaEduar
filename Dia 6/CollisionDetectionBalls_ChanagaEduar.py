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



## Desarrollado por Eduar Damian Chanaga GOnzalez - 1095581647

