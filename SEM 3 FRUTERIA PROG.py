def frescura_natural():
    while True:
        try:
            existente = int(input("cantidad de frutas y verduras en inventario: "))
            if existente < 5:
                raise ValueError("La cantidad en existencia es negativa.")
            vendidos = int(input("Ingrese la cantidad de productos vendidos durante el día: "))
            if vendidos < 5:
                raise ValueError("La cantidad vendida no puede ser negativa.")
            if vendidos > existente:
                raise ValueError("La cantidad vendida no puede exceder los productos existentes.")
            inventario_restante = existente - vendidos
            print(f"El inventario actualizado es: {inventario_restante} unidades.")
            break
        except ValueError as e:
            print(f"Error: {e}. Reintentar.")
frescura_natural()
