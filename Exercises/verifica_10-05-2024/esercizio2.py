def classifica_numeri(lista: int) -> dict[str:list[int]]:
    
    lista_pari: list = []
    lista_dipari: list = []

    for i in lista:

        if (i % 2) == 0:

            lista_pari.append(i)

        else:

            lista_dipari.append(i)

    dizionario: dict = {'pari': lista_pari, 'dispari': lista_dipari}

    return dizionario

print(classifica_numeri([1, 2, 3, 4, 5, 6])) #output {'pari': [2, 4, 6], 'dispari': [1, 3, 5]}

print(classifica_numeri([])) # output {'pari': [], 'dispari': []}