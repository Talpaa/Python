def lista_a_dizionario(tuples: list[tuple]) -> dict[str: int]:

    dizio: dict[str: int] = {}
    
    for tupla in tuples:

        if tupla[0] in dizio:

            dizio[tupla[0]] += tupla[1]

        else:

            dizio[tupla[0]] = tupla[1]

    return dizio

print(lista_a_dizionario([("a", 1), ("b", 2), ("c", 3)]))#{'a': 1, 'b': 2, 'c': 3}

print(lista_a_dizionario([("a", 1), ("a", 2), ("a", 3)]))#{'a': 6}