# Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Virjilio Ajila",
    "edad": 60,
    "ciudad": "Loja",
    "profesion": "Chofer Profesional"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo con una ciudad diferente
informacion_personal["ciudad"] = "Manabi"  # Cambiamos de Quito a Guayaquil

# Agregar una nueva clave-valor al diccionario (se asume que la clave "profesion" ya existe, así que agregamos una clave diferente)
informacion_personal["empresa"] = "Interciti SA"  # Añadimos una clave nueva llamada "empresa"

# Verificar si la clave "telefono" existe en el diccionario, si no existe, agregarla con un número ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"  # Agregamos un número ficticio

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminamos la clave "edad" porque ya no es necesaria

# Imprimir el diccionario final usando iteración para conocer cada clave y valor por separado
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")