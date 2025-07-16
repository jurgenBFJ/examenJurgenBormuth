productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0]
}

while True:
    print("\nMENU PRINCIPAL")
    print("1: Stock de la marca seleccionada")
    print("2: Búsqueda por precio (mínimo y máximo)")
    print("3: Actualizar precio de un modelo")
    print("4: Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        marca = input("Ingrese la marca: ")
        encontrados = False
        for modelo, datos in productos.items():
            if datos[0].lower() == marca:
                precio, cantidad = stock.get(modelo, ['N/A', 0])
                print(f"Modelo: {modelo} - Precio: {precio} - Stock: {cantidad}")
                encontrados = True
        if not encontrados:
            print("No se encontraron productos de esa marca.")

    elif opcion == '2':
        try:
            minimo = int(input("Precio mínimo: "))
            maximo = int(input("Precio máximo: "))
            encontrados = False
            for modelo, (precio, cantidad) in stock.items():
                if minimo <= precio <= maximo:
                    marca = productos.get(modelo, ['Desconocido'])[0]
                   
            if not encontrados:
                print("No se encontraron productos en ese rango de precio.")
        except ValueError:
            print("Ingrese valores numéricos válidos.")

    elif opcion == '3':
        while True:
            modelo = input("Ingrese el modelo a actualizar: ").strip()
            if modelo in stock:
                try:
                    nuevo_precio = int(input("Nuevo precio: "))
                    stock[modelo][0] = nuevo_precio
                    print(f"Precio actualizado para {modelo}: {nuevo_precio}")
                except ValueError:
                    print("Precio inválido. Debe ser un número.")
            else:
                print("Modelo no encontrado.")
            continuar = input("¿Desea actualizar otro precio? (s/n): ").strip().lower()
            if continuar != 's':
                break