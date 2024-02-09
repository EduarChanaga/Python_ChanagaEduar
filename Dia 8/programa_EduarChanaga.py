# ********************************************
# ********************************************
# ** Desde mi ordenador no funciona con ( ' )*
# ********************************************
# ********************************************

import json

# Abrir el archivo JSON
with open('datos.json', 'r') as Lospedidos:
    # Cargar el contenido del archivo en un diccionario
    diccionario = json.load(Lospedidos)


####################################### Funciones de eliminado y agregado de datos #############################################
def eliminar_cliente_por_id(id_cliente):
    # Eliminar el cliente de la lista de clientes
    diccionario['ventas']['clientes'] = [cliente for cliente in diccionario['ventas']['clientes'] if cliente['id'] != id_cliente]
    # Eliminar todos los pedidos relacionados con este cliente
    diccionario['ventas']['pedidos'] = [pedido for pedido in diccionario['ventas']['pedidos'] if pedido['id_cliente'] != id_cliente]

def agregar_nuevo_cliente(nuevo_cliente):
    # Obtener la lista de clientes y agregar el nuevo cliente
    diccionario['ventas']['clientes'].append(nuevo_cliente)

def eliminar_pedido_por_id(id_pedido):
    # Filtrar los pedidos que no tengan el ID proporcionado
    diccionario['ventas']['pedidos'] = [pedido for pedido in diccionario['ventas']['pedidos'] if pedido['id'] != id_pedido]

def agregar_pedido_para_cliente_existente(id_cliente, nuevo_pedido):
    # Buscar al cliente por su ID
    cliente_existente = next((cliente for cliente in diccionario['ventas']['clientes'] if cliente['id'] == id_cliente), None)
    if cliente_existente:
        # Verificar si la ID del comercial en el nuevo pedido es válida
        id_comercial_nuevo_pedido = nuevo_pedido.get('id_comercial', None)
        if id_comercial_nuevo_pedido is not None:
            comercial_existente = next((comercial for comercial in diccionario['ventas']['comerciales'] if comercial['id'] == id_comercial_nuevo_pedido), None)
            if comercial_existente:
                # Agregar el nuevo pedido al final de la lista de pedidos
                nuevo_pedido['id_cliente'] = id_cliente
                diccionario['ventas']['pedidos'].append(nuevo_pedido)
            else:
                print(f"No se encontró ningún comercial con el ID {id_comercial_nuevo_pedido}")
        else:
            print("La ID del comercial en el nuevo pedido no está especificada.")
    else:
        print(f"No se encontró ningún cliente con el ID {id_cliente}")

# Función para agregar un nuevo comercial
def agregar_nuevo_comercial(nuevo_comercial):
    # Obtener la lista de comerciales y agregar el nuevo comercial
    diccionario['ventas']['comerciales'].append(nuevo_comercial)

def eliminar_comercial_por_id(id_comercial):
    # Filtrar los comerciales que no tengan el ID proporcionado
    diccionario['ventas']['comerciales'] = [comercial for comercial in diccionario['ventas']['comerciales'] if comercial['id'] != id_comercial]

#################################### Impresion de los datos solicitados en la tarea 8 ##################################################
# Acceder a la parte de "pedidos" dentro de "ventas"
pedidos = diccionario["ventas"]["pedidos"]
comerciales = diccionario["ventas"]["comerciales"]
clientes = diccionario["ventas"]["clientes"]

while True:
    print("")
    print("\033[1;90mQue desea realizar?")
    print("1. Mostrar")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Agregar")
    decision3=int(input("--> "))
    if decision3 == 1:
        print("Que desea ver?")
        print("1. Los pedidos en orden de fecha (comenzando desde el más reciente)")
        print("2. Los pedidos de mayor valor ")
        print("3. Los clientes que han realizado compras")
        print("4. Los pedidos realizados en 2017, cuya cantidad total es superior a 500€")
        print("5. Los comerciales con comisión entre 0.05 y 0.11")
        print("6. El valor de la comisión más alto en la tabla comercial")
        print("7. Clientes de Sevilla ordenados alfabéticamente por apellidos y nombre")
        print("8. Listado de nombres de clientes que empiezan por A y terminan por n, o empiezan por P")
        print("9. Listado de nombres de clientes que empiezan por A")
        print("10. Listado de nombres de comerciales con apellido 'Ruiz'")
        print("11. Ver clientes")
        print("12. Ver pedidos")
        print("13. Ver comerciales")
        decision=int(input("--> "))

        if decision == 1:##############################################################################################################################
            # Ordenar los pedidos por fecha en orden descendente
            pedidos_ordenados = sorted(pedidos, key=lambda x: x['fecha'], reverse=True)
            # Imprimir los pedidos en orden de fecha, comenzando desde el más reciente
            print("Los pedidos en orden de fecha (comenzando desde el más reciente) son:")
            for i in pedidos_ordenados:
                print(i)

        elif decision ==2:##############################################################################################################################
            pedidos_mayorvalor=sorted(pedidos, key=lambda x: x['total'], reverse=True)
            print("Los pedidos de mayor valor son:")
            for i in pedidos_mayorvalor[:2]:
                print(i)
            print("")

        elif decision==3:##############################################################################################################################
            lista_ids_clientes = []
            for pedido in pedidos:
                id_cliente = pedido["id_cliente"]
                if id_cliente not in lista_ids_clientes:
                    lista_ids_clientes.append(id_cliente)
            # Imprimimos la lista de IDs de los clientes
            print("Los clientes que han realizado compras son:")
            print(lista_ids_clientes)
        elif decision==4:##############################################################################################################################
            # Filtrar los pedidos que se realizaron en <link>2017</link> y cuya cantidad total sea superior a 500€
            pedidos_2017_mayor_500 = [i for i in pedidos if i["fecha"].startswith("2017") and i["total"] > 500]                 
            #El método ".startswith()" es una función integrada de Python que se utiliza para verificar si una cadena de texto comienza con ciertos caracteres específicos. Su sintaxis es la siguiente
            print("")  
            # Imprimir los pedidos que cumplen con los criterios
            print("Los pedidos realizados en 2017, cuya cantidad total es superior a 500€ son:")
            for i in pedidos_2017_mayor_500:
                print(i)
        elif decision==5:##############################################################################################################################
            # Imprimir los nombres y apellidos de los comerciales seleccionados
            print("")
            comerciales_seleccionados = [i for i in comerciales if 0.05 <= i["comision"] <= 0.11]
            print("Los comerciales con comisión entre 0.05 y 0.11 son:")
            for i in comerciales_seleccionados:
                nombre = i["nombre"]
                apellido1 = i["apellido1"]
                apellido2 = i.get("apellido2", "")  # Si no hay segundo apellido, se asigna una cadena vacía
                print(f"{nombre} {apellido1} {apellido2}")
        elif decision==6:##############################################################################################################################
            # Inicializar el valor máximo de la comisión
            max_comision = float('-inf')  # Inicializado con el valor negativo infinito
            # Iterar sobre la lista de comerciales y actualizar el valor máximo de la comisión
            for i in comerciales:
                comision = i.get("comision", 0)  # Si no hay comisión, se asigna un valor predeterminado de 0
                if comision > max_comision:
                    max_comision = comision

            # Imprimir el valor máximo de la comisión
            print("")
            print("El valor de la comisión más alto en la tabla comercial es:", max_comision)
            print("")
        elif decision==7:##############################################################################################################################
            # Filtrar los clientes cuya ciudad sea "Sevilla"
            clientes_sevilla = [i for i in clientes if i.get("ciudad", "") == "Sevilla"]

            # Ordenar los clientes alfabéticamente por apellidos y nombre
            clientes_sevilla_ordenados = sorted(clientes_sevilla, key=lambda x: (x["apellido1"], x["nombre"]))

            # Imprimir el identificador, nombre y primer apellido de los clientes de Sevilla ordenados
            print("Clientes de Sevilla ordenados alfabéticamente por apellidos y nombre:")
            for i in clientes_sevilla_ordenados:
                identificador = i["id"]
                nombre = i["nombre"]
                apellido1 = i["apellido1"]
                print(f"ID: {identificador}, Nombre: {nombre}, Apellido: {apellido1}")
        elif decision==8:##############################################################################################################################
            # Filtrar los nombres que empiezan por "A" y terminan por "n"
            nombres_A_n = [i["nombre"] for i in clientes if i["nombre"].startswith("A") and i["nombre"].endswith("n")]

            # Filtrar los nombres que empiezan por "P"
            nombres_P = [i["nombre"] for i in clientes if i["nombre"].startswith("P")]

            # Combinar y ordenar alfabéticamente los nombres de ambos grupos
            nombres_ordenados = sorted(nombres_A_n + nombres_P)
            print("")
            # Imprimir el listado de nombres ordenados alfabéticamente
            print("Listado de nombres de clientes que empiezan por A y terminan por n, o empiezan por P:")
            for i in nombres_ordenados:
                print(i)


            
        elif decision==9:##############################################################################################################################
            # Imprimir el listado de nombres ordenados alfabéticamente
            nombres_A_n = [cliente["nombre"] for cliente in clientes if cliente["nombre"].startswith("A")]
            print("")
            print("Listado de nombres de clientes que empiezan por A ")
            for nombre in nombres_A_n:
                print(nombre)


        

            # Imprimir el listado de nombres de los comerciales que tienen como apellido "Ruiz"
        elif decision==10:##############################################################################################################################
        # Filtrar los comerciales cuyo apellido sea "Ruiz" y obtener sus nombres
            nombres_ruiz = {comercial["nombre"] for comercial in comerciales if comercial.get("apellido1", "") == "Ruiz"}
            print("")
            print("Listado de nombres de comerciales con apellido 'Ruiz':")
            for nombre in nombres_ruiz:
                print(nombre)

        elif decision==11:
            for i in clientes:
                print(i)
        elif decision==12:
            for i in pedidos:
                print(i)
        elif decision==13:
            for i in comerciales:
                print(i)
        else:
            break
        print("")
        print("")
        ### Decision de modificar ###
        
    elif decision3==2:






######################### MODIFICAR clientes #########################
        print("\033[93m1. Modificar datos de cliente ( Nombre/ Apellido/ Apellido2/ ciudad )")
        print("2. Modificar pedidos ( Total / fecha )")
        print("3. Modificar datos de comerciales ( nombre / apellido1 / apellido2 / comision )")
        print("4. Salir")
        decision4=int(input("--> "))
        if decision4==1:
            for i in clientes:
                            print(i)
            print("")
            id_cliente_mod=int(input("Id del usuario a modificar: "))
            nombre_cliente_mod=str(input("Nombre: "))
            apellido_cliente_mod=str(input("Apellido: "))
            apellido2_cliente_mod=str(input("Apellido 2: "))
            ciudad_cliente_mod=str(input("Ciudad: "))
    # Iterar sobre la lista de clientes y modificar los nombres
            for cliente in diccionario['ventas']['clientes']:
                if cliente['id'] == id_cliente_mod:  # Modificar el nombre del cliente con ID 4
                    cliente['nombre'] = nombre_cliente_mod
                    cliente['apellido1'] = apellido_cliente_mod
                    cliente['apellido2'] = apellido2_cliente_mod
                    cliente["ciudad"]=ciudad_cliente_mod
            # Guardar los cambios en el mismo JSON (sobreescribir)
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)



######################### MODIFICAR pedidos #########################
        if decision4==2:
            for i in pedidos:
                            print(i)
            print("")
            id_cliente_mod=int(input("Id del pedido a modificar: "))
            
            total_pedido_mod=float(input("Total: "))
            print("fecha = año-mes-dia Ej: (2018-10-06)")
            fecha_pedido_mod=str(input("Fecha: "))

            
    # Iterar sobre la lista de clientes y modificar los nombres
            for pedido in diccionario['ventas']['pedidos']:
                if pedido['id'] == id_cliente_mod:  # Modificar el nombre del cliente con ID 4
                    pedido['total'] = total_pedido_mod
                    pedido["fecha"]=fecha_pedido_mod
  
            # Guardar los cambios en el mismo JSON (sobreescribir)
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)




######################### MODIFICAR comerciales #########################
        if decision4==3:
            for i in comerciales:
                            print(i)
            print("")
            id_comercial_mod=int(input("Id del comercial: "))
            
            nombre_comercial_mod=str(input("Nombre del comercial: "))
            apellido1_comercial_mod=str(input("Apellido del comercial: "))
            apellido2_comercial_mod=str(input("Apellido2 del comercial: "))

            while True:
                try: #Comprobar que el numero este entre el rango 1-1000 y que no tenga decimales.
                    comision_comercial_mod=float(input("Comision < 1: "))
                    if comision_comercial_mod < 1 :
                        break  
                    else:
                        print("Por favor digite una comision menor a 1")
                except ValueError:
                    print(" ")            
    # Iterar sobre la lista de clientes y modificar los nombres
            for comercial in diccionario['ventas']['comerciales']:
                if comercial['id'] == id_comercial_mod:  # Modificar el nombre del cliente con ID 4
                    comercial['nombre'] = nombre_comercial_mod
                    comercial["apellido1"]=apellido1_comercial_mod
                    comercial["apellido2"]=apellido2_comercial_mod
                    comercial["comision"]=comision_comercial_mod
  
            # Guardar los cambios en el mismo JSON (sobreescribir)
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)
        if decision4==4:
            print("")





############################################ ELIMINAR ############################################
    elif decision3==3:
        print("\033[91m1. Eliminar datos de cliente segun id")
        print("2. Eliminar pedido")
        print("3. Eliminar comercial")
        print("4. Salir")
        decision5=int(input("--> "))
        if decision5==1:
            for i in clientes:
                print(i)
            print("")
            id_cliente_a_eliminar=int(input("Id del cliente a eliminar: "))
            eliminar_cliente_por_id(id_cliente_a_eliminar)
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)

        if decision5==2:
            # ID del pedido que deseas eliminar
            for i in pedidos:
                print(i)
            print("")
            id_pedido_a_eliminar = int(input("ID del pedido que desea eliminar: "))

            # Eliminar el pedido por su ID
            eliminar_pedido_por_id(id_pedido_a_eliminar)

            # Guardar los cambios en el archivo JSON
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)
        if decision5==3:
            # ID del comercial que deseas eliminar
            for i in comerciales:
                print(i)
            print("")
            id_comercial_a_eliminar = int(input("Ingrese la ID del comercial que desea eliminar: "))

            # Eliminar el comercial por su ID
            eliminar_comercial_por_id(id_comercial_a_eliminar)

            # Guardar los cambios en el archivo JSON
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)


        if decision5==4:
            print("")




############################################ AGREGAR ############################################
    elif decision3==4: 
        print("\033[92m1. Agregar nuevo cliente")
        print("2. Agregar nuevo pedido")
        print("3. Agregar nuevo comercial")
        print("4. Salir")
        decision5=int(input("---> "))
        if decision5==1:
            for i in clientes:
                print(i)
            print("")
            id=int(input("Nueva id: "))
            name=str(input("Nombre cliente: "))
            ape1=str(input("Apellido cliente: "))
            ape2=str(input("Apellido 2 cliente: "))
            ciudad=str(input("Ciudad cliente: "))
            categoria=int(input("Categoria cliente: "))
            nuevo_cliente = {
                "id": id,
                "nombre": name,
                "apellido1": ape1,
                "apellido2": ape2,
                "ciudad": ciudad,
                "categoría": categoria
            }

            # Agregar el nuevo cliente
            agregar_nuevo_cliente(nuevo_cliente)

            # Guardar los cambios en el archivo JSON
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)

        if decision5==2:
            for i in pedidos:
                print(i)
            print("")
            # ID del cliente existente para el cual deseas agregar el pedido
            id_cliente_existente = int(input("ID cliente que realiza el pedido:"))
            # Crear un nuevo pedido
            id_cliente_pedido=int(input("Id del nuevo pedido: "))
            total_cliente_pedido=float(input("Total del nuevo pedido: "))
            año=str(input("Año del pedido: "))
            mes=str(input("Mes del pedido: "))
            dia=str(input("Dia del pedido: "))
            id_comercial_pedido=int(input("Id del comercial: "))
            gion=str("-")
            nuevo_pedido = {
                "id": id_cliente_pedido,
                "total": total_cliente_pedido,
                "fecha": año+gion+mes+gion+dia,
                "id_comercial": id_comercial_pedido
            }


            # Agregar el nuevo pedido para el cliente existente
            agregar_pedido_para_cliente_existente(id_cliente_existente, nuevo_pedido)

            # Guardar los cambios en el archivo JSON
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)

        if decision5==3:
            for i in comerciales:
                print(i)
            print("")
            id_new_comercial=int(input("Nueva id comercial: "))
            name_new_comercial=str(input("Nombre comercial: "))
            ap1_new_comercial=str(input("Apellido comercial: "))
            ap2_new_comercial=str(input("Apellido 2 comercial: "))
            while True:
                try: #Comprobar que el numero este entre el rango 1-1000 y que no tenga decimales.
                    comision_new_comercial=float(input("Comision comercial: "))
                    if comision_new_comercial < 1 :
                        break  
                    else:
                        print("Por favor digite una comision menor a 1")
                except ValueError:
                    print(" ")    
            # Crear un nuevo comercial
            nuevo_comercial = {
                "id": id_new_comercial,
                "nombre": name_new_comercial,
                "apellido1": ap1_new_comercial,
                "apellido2": ap2_new_comercial,
                "comision": comision_new_comercial
            }

            # Agregar el nuevo comercial
            agregar_nuevo_comercial(nuevo_comercial)

            # Guardar los cambios en el archivo JSON
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)
        if decision5==4:
            print("")
## Desarrollado por Eduar Damian Chanaga Gonzalez - 1095581647