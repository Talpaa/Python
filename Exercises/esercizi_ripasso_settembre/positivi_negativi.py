def classifica_numeri(lista: int) -> dict[str:list[int]]:

    dizio: dict[str: list[int]] = {'positivi': [], 'negativi': []}

    for num in lista:

        if num >= 0:

            dizio['positivi'].append(num)

        else:

            dizio['negativi'].append(num)

    return dizio