# Almacena los productos con su respectivo precio en un diccionario.
panaderia = {"inventario": ("rosquilla", "cascarita", "churros", "pan de queso"),
            "Precios": (3000, 1000, 2500, 2000)
            }

# Muestra el menú
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
