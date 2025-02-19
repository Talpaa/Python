def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:

    for key in da_rimuovere:

        for i in range(da_rimuovere[key]):

            if key in lista:

                lista.remove(key)

    return lista

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2})) #output [1, 3, 4]

print(rimuovi_elementi([], {2: 1})) #output []

 	

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 1})) #output [1, 3, 2, 4]

print(rimuovi_elementi([1, 1, 1, 1], {1: 2})) #output [1, 1]

