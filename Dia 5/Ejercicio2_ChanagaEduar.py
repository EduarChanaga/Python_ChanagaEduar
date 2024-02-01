# m = monedas
# me = mesas
# mo = lista para almacenar las diferentes longitudes de monedas
# me2 = lista para almacenar la altura de las patas de las mesas deseadas

def maximo(maxcoins):
    print("hi")
    print(maxcoins)

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
maxcoins = max(mo)

while True:
    element=me2[count]
    if log>=element:
        break
    else:
        log=maxcoins+log
        print(log)

    count=count+1
    
#programacion de mrd .i.