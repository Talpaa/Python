def remove_duplicates(lista: list) -> list:
    
    new_lista: list = []
    
    for i in lista:

        if i not in new_lista:

            new_lista.append(i)

    return new_lista

    return lista


lista = [1,6,7,2,3,3,4,5,5,8,9,0,0,0,0,0,]


lista_senza_duplicati = remove_duplicates(lista)

print(lista_senza_duplicati)