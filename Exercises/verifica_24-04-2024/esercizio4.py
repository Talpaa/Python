
#crea una lista di tutti i divisori del numero inserito
def divisors(n):
    result = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            result.append(i)
    result.append(n)
    return result

#formula che ti permette di partire da un numero e ti trova i due numeri interi più grandi che se moltiplicati tra di loro danno ilnumero di partenza
def construct_rectangle(area: float) -> list[float]:

    lista: list = []
    max: int = area
    dividers : list = divisors(area)
    lato_lungo: int = 0
    lato_corto: int = 0
    
    min_dist = area - 1
    for l in dividers:

        for c in dividers:

            if (l * c) == area and l >= c:

                lato_lungo = l
                lato_corto = c
                
                dist = abs(lato_lungo - lato_corto)
                
                if dist <= min_dist:
                    min_dist = dist
                    lista = [lato_lungo, lato_corto]

    return lista

        




print(construct_rectangle(122122)) #risultato [2, 2]