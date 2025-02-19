def frequency_dict(lista: list[str])->dict[int: str]:

    dizio: dict[int: str] = {}

    for x in lista:

        if x in dizio:

            dizio[x] += 1

        else:

            dizio[x] = 1

    return dizio

print(frequency_dict(['mela', 'banana', 'mela']))#{'mela': 2, 'banana': 1}