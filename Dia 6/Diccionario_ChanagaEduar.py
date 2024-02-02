panaderia = {"Inventario": ("rosquilla", "Cascarita", "churros", "Pan de queso"),
            "Precios": (3000, 1000, 2500, 2000)}

# Muestra el menú
print("Menu actual:")
print(panaderia)

p = str(input("Ingrese lo que desea comprar de la lista anterior: "))
c = int(input("Ingrese la cantidad que desea de este producto: "))


if p in panaderia["Inventario"]:
                        #.index se usa para obtener la posición del producto p en la lista de inventario.
    index = panaderia["Inventario"].index(p)
   
    precio = panaderia["Precios"][index]
   
    print(f"{p} - Precio: {precio*c} - Cantidad: {c}")
else:
    print(f"{p} no está en el inventario.")
