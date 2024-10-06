# Definimos el nombre del archivo
file_name = "my_notes.txt"

# Abrimos el archivo en modo escritura (esto crea el archivo)
archivo_escritura = open(file_name, "w")

# Escribimos algunas líneas en el archivo
archivo_escritura.write("linea 1: Mi personalidad es carismática\n")  # Cerrado el paréntesis
archivo_escritura.write("linea 2: Amo bailar\n")  # Cerrado el paréntesis

# También podemos escribir varias líneas a la vez
lineas = ["linea 3: Dibujar en mis momentos libres me relaja\n", "linea 4: La música me inspira\n"]
archivo_escritura.writelines(lineas)  # Usar writelines() correctamente

# Cerramos el archivo de escritura
archivo_escritura.close()

# Leemos y abrimos el archivo en modo lectura para leer lo que contiene
archivo_lectura = open(file_name, "r")

# Leemos y mostramos cada línea en la consola
for line in archivo_lectura:  # Consistencia en minúsculas
    print(line.strip())  # Usamos strip() para quitar el salto de línea

# Cerramos el archivo de lectura
archivo_lectura.close()