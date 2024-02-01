from functools import reduce
from math import gcd
# m = monedas
# me = mesas
# mo = lista para almacenar las diferentes longitudes de monedas
# me2 = lista para almacenar la altura de las patas de las mesas deseadas
def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

def find_lcm_of_list(list):
    return reduce(lcm, list)

# Ejemplo de uso:



m, me = map(int, input("Enter m and me: ").split())
mo = []
me2 = []
me3=[]
log = 0  # No es necesario usar int(0), ya que log es un entero.
count=0
for i in range(m):
    mo.append(int(input()))
for i in range(me):
    me2.append(int(input()))

# Mostrar las listas
print("monedas:", mo)
print("mesas:", me2)

resultado = find_lcm_of_list(mo)
print(f"El mínimo común múltiplo de {mo} es: {resultado}")