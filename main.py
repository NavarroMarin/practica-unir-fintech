"""
License: Apache
Organization: UNIR
practica: 1
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False

"""
Ordena una lista de elementos.

Args:
    items (list): Lista de elementos a ordenar.
    ascending (bool): Si es True, ordena de manera ascendente; si es False, descendente.

Returns:
    list: Lista ordenada.
    
Raises:
    RuntimeError: Si el parámetro 'items' no es una lista.
"""
def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))


"""
Elimina elementos duplicados de una lista.

Args:
    items (list): Lista de elementos, posiblemente con duplicados.

Returns:
    List: Lista sin elementos duplicados.
"""
def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list))
