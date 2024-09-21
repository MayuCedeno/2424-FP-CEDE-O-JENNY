# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento = 15):
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento


# Función principal
def main():
    # Primera llamada: solo se proporciona el monto total de la compra
    monto1 = 2000  # Monto total de la compra
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1
    print(f"Compra 1: Monto total: ${monto1}, Descuento: ${descuento1}, Monto final: ${monto_final1}")

    # Segunda llamada: se proporciona el monto total y el porcentaje de descuento
    monto2 = 2000  # Monto total de la compra
    porcentaje_descuento2 = 20  # Porcentaje de descuento
    descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
    monto_final2 = monto2 - descuento2
    print(f"Compra 2: Monto total: ${monto2}, Descuento: ${descuento2}, Monto final: ${monto_final2}")


# Ejecutar el programa principal
main()