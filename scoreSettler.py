scores = \
    [874300, 879200, 1172100, 1141800, 933900, 1177200, 1190200, 1110100, 1158400, 985600, 1047200, 1049100, 1138600
        ,1170500, 1064500, 1190000, 1050200, 1090400, 1062800, 1061700, 1218000, 1068000, 1127700, 1144800, 1195100]


def qs(lista:list, lim_izq:int, lim_der:int) -> None:
    """This function is the recursive representation of a quicksort
    algorithm.

    Args:
        lista (list): list to sort
        lim_izq (int): left limit to evaluate
        lim_der (int): right limit to evaluate
    """
    pivote = int((lim_izq + lim_der) / 2)
    derecha = lim_der
    izquierda = lim_izq

    while izquierda <= derecha:

        while lista[izquierda] < lista[pivote]:
            izquierda += 1

        while lista[derecha] > lista[pivote]:
            derecha -= 1

        if izquierda <= derecha:
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
            izquierda += 1
            derecha -= 1

    if izquierda < lim_der:
        qs(lista, izquierda, lim_der)

    if derecha > lim_izq:
        qs(lista, lim_izq, derecha)


def quicksort(Lista:list, ascendent:bool = True):
    """This is the wrapper to call a quicksort implementation.

    Args:
        Lista (list): List to sort
        ascendent (bool, optional): determines if the result is returned in ascendant mode. Defaults to True.

    Returns:
        [list]: Sorted List
    """
    sorted_list = [element for element in Lista]
    qs(sorted_list, 0, (len(sorted_list) - 1))
    if ascendent:
        return sorted_list
    else:
        return sorted_list[::-1]


def scoreSettler(score_list:list, max_score:int):
    """this function will take a list of unsorted scores plus the highest possible score 
    and return a sorted list of all of the scores, in descending order from high score to low score

    Args:
        score_list (list): [description]
        max_score (int): [description]

    Returns:
        [list]: sorted score list
    """
    return quicksort(score_list, False)


if __name__ == '__main__':
    result = scoreSettler(scores, 1218000)
    print(scores)
    print(result)