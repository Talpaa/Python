def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:

    dizionario: dict[str,list[int]] = {}
    
    for x in tuples:

        for y in range(1,len(x)):

            if x[0] in dizionario:
                
                dizionario[x[0]].append(x[y])

            else:
                dizionario[x[0]] = [x[y]]

    return dizionario
        


print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))#{'a': [1, 3], 'b': [2]}
print(lista_a_dizionario([]))#{}

	

