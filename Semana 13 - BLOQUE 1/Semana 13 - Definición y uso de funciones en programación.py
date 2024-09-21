def temperatura_promedio(ciudades_temperaturas):
    temperaturas_promedio = {}
    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio[ciudad] = promedio
    return temperaturas_promedio


# Creamos un diccionario de ciudades y temperaturas
ciudades_temperaturas = {ç
    "Santo Domingo": [79, 61, 77, 86, 53],
    "Guayaquil": [68, 69, 88, 79, 87],
    "Cuenca": [55, 48, 74, 55, 73],

}

# Llamamos a la función para calcular las temperaturas promedio
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

# Mostramos los resultados
print("Temperaturas Promedio por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {promedio:.2f}°C")