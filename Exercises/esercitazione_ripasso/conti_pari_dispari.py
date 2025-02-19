def classifica_numeri(lista: list)->dict[str:list[int]]:

    dizio: dict[str:list[int]] = {'pari': [], 'dispari': []}

    for num in lista:

        if (num % 2) == 0:

            dizio['pari'].append(num)

        else:

            dizio['dispari'].append(num)

    return dizio

print(classifica_numeri([1, 2, 3, 4, 5, 6]))#{'pari': [2, 4, 6], 'dispari': [1, 3, 5]}

print(classifica_numeri([]))#{'pari': [], 'dispari': []}