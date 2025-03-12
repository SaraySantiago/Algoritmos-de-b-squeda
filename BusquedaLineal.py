def busqueda_lineal(lista, elemento):
  """
  Busca un elemento en una lista usando búsqueda lineal.

  Args:
    lista: La lista en la que buscar.
    elemento: El elemento a buscar.

  Returns:
    El índice del elemento si se encuentra, o -1 si no se encuentra.
  """

  for i in range(len(lista)):
    if lista[i] == elemento:
      return i  # Se encontró el elemento en el índice i
  return -1  # El elemento no se encontró en la lista

# Ejemplo de uso
mi_lista = [10, 25, 5, 30, 15]
elemento_buscado = 30

indice = busqueda_lineal(mi_lista, elemento_buscado)

if indice != -1:
  print(f"El elemento {elemento_buscado} se encontró en el índice {indice}")
else:
  print(f"El elemento {elemento_buscado} no se encontró en la lista")


