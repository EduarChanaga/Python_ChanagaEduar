import json

# Abrir el archivo JSON
with open('data.json', 'r') as Lospedidos:
    # Cargar el contenido del archivo en un diccionario
    diccionario = json.load(Lospedidos)

# Acceder a la parte de "pedidos" dentro de "ventas"
pedidos = diccionario["ventas"]["pedidos"]


# Ordenar los pedidos por fecha en orden descendente

pedidos_ordenados = sorted(pedidos, key=lambda x: x['fecha'], reverse=True)
pedidos_mayorvalor=sorted(pedidos, key=lambda x: x['total'], reverse=True)


# Imprimir los pedidos en orden de fecha, comenzando desde el más reciente
print("Los pedidos en orden de fecha (comenzando desde el más reciente) son:")
for i in pedidos_ordenados:
    print(i)
print("")
print("Los pedidos de mayor valor son:")
for i in pedidos_mayorvalor[:2]:
    print(i)
lista_ids_clientes=[]
print("")
print("Los clientes que han realizado compras son:")
for i in pedidos:
    lista_ids_clientes.append(i["id_cliente"])  #falta eliminar iguales
print(lista_ids_clientes)

# Imprimimos la lista de IDs de los clientes


## Desarrollado por Eduar Damian Chanaga GOnzalez - 1095581647