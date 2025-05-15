"""
Recibe una frase y separa las palabras largas de la frase. 
Devuelve en una lista separada solo las que tienen más de 5 letras.
"""

def palabras_largas(frase):
    """
    Función que recibe una frase y devuelve una lista con las palabras que tienen más de 5 letras.
    
    :param frase: str, la frase a analizar
    :return: list, lista de palabras largas
    """
    # Separamos la frase en palabras
    palabras = frase.split()
    
    # Filtramos las palabras que tienen más de 5 letras
    palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]
    
    return palabras_largas