"""
Data una lista di numeri interi, riordina i numeri in modo che tutti i numeri pari appaiano prima di tutti i numeri dispari. Restituisce l'elenco riorganizzato.
"""

def even_odd_pattern(nums: list[int]) -> list[int]:

    lista_pari: list = []

    lista_dispari: list = []

    for i in nums:

        if (i % 2) == 0:

            lista_pari.append(i)

        else:

            lista_dispari.append(i)


    nums = lista_pari + lista_dispari

    return nums





print(even_odd_pattern([3, 6, 1, 8, 4, 7]))