def count_isolated(lista: list) -> int:
    
    count: int = 0
    num: int = (len(lista)-1)
    for i in range(0 , num):

        if i == 0:

            if (lista[i+1] != lista[i]):

                count += 1

        else:

            if (lista[i-1] != lista[i])and(lista[i+1] != lista[i]):

                count += 1

        if i == num-1:

            if (lista[i] != lista[i+1]):

                count += 1

    return count


print(count_isolated([1, 2, 2, 3, 3, 3, 4]))

#print(count_isolated([1, 2, 3, 4, 5]))