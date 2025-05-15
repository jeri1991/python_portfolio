def formateador_nombres(lista_nombres):
    """
    Recibe una lista de nombres desordenados y los formatea eliminando espacios innecesarios
    y ajustando las mayúsculas y minúsculas para que cada palabra comience con mayúscula.
    """
    nombres_formateados = []
    for nombre in lista_nombres:
        nombre_limpio = nombre.strip().title()
        nombres_formateados.append(nombre_limpio)
    return nombres_formateados

print(formateador_nombres(["  juan perez ", "maria gonzalez", "  luis fernando  ", "  ana   "]))