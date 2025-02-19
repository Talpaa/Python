"""
Nel gioco del blackjack, il valore di una mano è determinato dalla somma dei valori delle carte. Ogni carta ha un valore compreso tra 2 e 11 compresi. 
Tuttavia, se una mano contiene un asso, il valore dell'asso può essere 1 o 11, a seconda di quale sia più favorevole al giocatore in quel momento. 
Dato un elenco di valori delle carte che rappresentano una mano di blackjack, scrivi una funzione per determinare il valore totale della mano.
"""

def blackjack_hand_total(cards: list[int]) -> int:
    
    n: int = 0
    totale: int = 0

    for i in cards:

        if (i == 1)or(i == 11):

            n +=1

        else:

            totale += i
    
    if n == 1:

        if (totale + 11) > 21:

            totale += 1

        else:
            totale += 11 

    elif n > 1:

        totale += (n-1)

        if (totale + 11) > 21:

            totale += 1

        else:

            totale += 11
        


    return totale



print(blackjack_hand_total([2, 3, 5]))  #risultato 10

print(blackjack_hand_total([11, 5, 5])) #risultato 21

print(blackjack_hand_total([1, 10, 11]))    #risultato 12

print(blackjack_hand_total([1, 10, 5])) #risultato 16

print(blackjack_hand_total([11, 5, 3])) #risultato 19