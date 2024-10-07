inventario = []
def bubble_sort(inventario : list):
    for i in range (len(inventario) - 1):
        for j in range(len(inventario) -1 - i):
            if inventario[j][1] > inventario[j+1][1]:
                inventario[j], inventario[j + 1] = inventario[j + 1], inventario[j]
    return inventario

def mostrar_menu ():
    print("""
    [1] Cargar Producto
    [2] Buscar Producto
    [3] Ordenar inventario
    [4] Ver producto mas caro y barato
    [5] Salir
          """)
    seleccion = int(input(" "))
    return seleccion

def menu():
    seguir = "s"
    while seguir == "s":
        num = mostrar_menu()
        match num:
            case 1: cargar_producto(inventario)
            case 2: buscar_producto(inventario)
            case 3: ordenar_inventario (inventario)
            case 4: top_low_productos(inventario)
            case 5: seguir = "n"
            case _: print("Ingresar una opcion valida")

def cargar_producto(inventario : list, nombre : str = "", precio : float = 0, cantidad : int = 0):
    print("Agregando nuevo producto... \n")
    nombre = input("Nombre del producto: ")
    nombre = nombre.capitalize()
    precio = float(input("Ingrese el precio del producto: "))
    while precio < 1:
        precio = float(input("Ingrese un precio válido no menor a 0: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    while cantidad < 1:
        cantidad = int(input("Ingrese una cantidad válida no menor a 0: "))
    elementos = [nombre, precio, cantidad]
    inventario.append(elementos)
    print(inventario)
    return inventario   
def buscar_producto(inventario : list, nombre : str = ""):
    nombre = input("Nombre del producto que desea buscar: ").capitalize()
    existe = False
    indice = None
    for i in range(len(inventario)):
        if nombre == inventario[i][0]:
            existe = True
            indice = i
        else: print("No se ha encontrado ese producto.")
        if existe:
            print("------------------------------------------------------------------")
            print(f"Se ha encontrado el producto \nNombre:{inventario[indice][0]}\nPrecio: {inventario[indice][1]}\nCantidad: {inventario[indice][2]}")
            print("------------------------------------------------------------------")
def ordenar_inventario(inventario):
    for i in range (len(inventario) - 1):
        for j in range(len(inventario) -1 - i):
            if inventario[j][1] > inventario[j+1][1]:
                inventario[j], inventario[j + 1] = inventario[j + 1], inventario[j]
    print(f"Se ha ordenado el inventario {inventario}")
    return inventario
def top_low_productos(inventario : list):
    mas_caro = float("-inf")
    mas_barato = float("inf")
    caro_nombre = ""
    barato_nombre = ""
    for i in range(len(inventario)):
        if inventario[i][1] > mas_caro:
            mas_caro = inventario[i][1]
            caro_nombre = inventario[i][0]
        if inventario[i][1] < mas_barato:
            mas_barato = inventario[i][1]
            barato_nombre = inventario[i][0]
    print(f"El producto mas barato es {barato_nombre} y el más caro es {caro_nombre}")
menu()
