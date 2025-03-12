def busqueda_binaria(lista, elemento):
    """
    Busca un elemento en una lista ordenada usando búsqueda binaria.

    Args:
        lista: La lista ordenada en la que buscar.
        elemento: El elemento a buscar.

    Returns:
        El índice del elemento si se encuentra, o -1 si no se encuentra.
    """

    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2  # Calcula el índice medio
        if lista[medio] == elemento:
            return medio  # Se encontró el elemento en el índice medio
        elif lista[medio] < elemento:
            izquierda = medio + 1  # Busca en la mitad derecha
        else:
            derecha = medio - 1  # Busca en la mitad izquierda

    return -1  # El elemento no se encontró en la lista

# Ejemplo de uso
mi_lista = [5, 10, 15, 20, 25, 30]  # Lista ordenada
elemento_buscado = 20

indice = busqueda_binaria(mi_lista, elemento_buscado)

if indice != -1:
    print(f"El elemento {elemento_buscado} se encontró en el índice {indice}")
else:
    print(f"El elemento {elemento_buscado} no se encontró en la lista")