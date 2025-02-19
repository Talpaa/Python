def trova_tutte_chiavi(dizio: dict[str: int], num: int)->list[str]:

    lista: list = []

    for key in dizio:

        if dizio[key] == num:

            lista.append(key)

    return lista
print(trova_tutte_chiavi({'a': 1, 'b': 2, 'c': 1}, 1))#['a', 'c']
print(trova_tutte_chiavi({}, 1))#[]