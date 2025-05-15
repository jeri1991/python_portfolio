def histograma_vocales(texto):
  #Define el histograma de vocales a medir
  histograma = [['a', 0], ['e', 0], ['i', 0], ['o', 0], ['u', 0]]
  
  #Normaliza caracteres acentuados 
  texto = texto.lower()
  texto = texto.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ü', 'u')

  '''
  Itera sobre el texto y compara el primer elemento de cada sublista con cada
  letra del texto. Si la letra es igual al primer elemento de la sublista,
  se incrementa en uno el segundo elemento de la sublista.
  Retorna el histograma para reutilizarlo en caso de ser necesario.
  '''
  for letter in texto:
    for item in histograma:
      if letter == item[0]:
        item[1] += 1
  return histograma

string1 = "Un pequeño muchachito, güerito, güerito."
string2 = "murciélago"
string3 = "Anita lava la tina"
print(histograma_vocales(string1))
print(histograma_vocales(string2))
print(histograma_vocales(string3))