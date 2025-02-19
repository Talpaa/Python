"""
Immagina di avere uno scrigno pieno di gioielli (rappresentati da una lista di numeri interi). 
Questi gioielli hanno vari valori, alcuni più preziosi di altri. Il tuo compito è trovare il terzo gioiello distinto più prezioso nello scrigno.

Qual è la svolta?

Nello scrigno possono esserci gioielli duplicati (numeri con lo stesso valore). 
A noi però interessano solo valori distinti, ovvero gioielli con valori unici.

Scrivi una funzione che prenda come input questo array di valori di gioielli (numeri). Se nello scrigno sono presenti almeno tre valori distinti, 
la funzione dovrebbe restituire il valore del terzo gioiello distinto di maggior valore.

Ma c'è un problema!

Se non ci sono tre valori distinti (ad esempio, solo due valori univoci o tutti i valori sono uguali), 
la funzione dovrebbe restituire il valore del gioiello più prezioso nello scrigno.
"""

def third_max(nums: list[int]) -> int:

    first_max: int =nums[0]
    second_max = third_max = None

    n: int = 1

    if len(nums) >= 3:

        while (second_max == None):

            if nums[n] != first_max:

                second_max = nums[n]
                n +=1

            else:
                n += 1

                
        while (third_max == None)and(n < len(nums)):


            if (nums[n] != first_max) and (nums[n] != second_max):

                third_max = nums[n]

            else:
                n += 1

    else:

        third_max = nums[-1]



    if third_max == None:
    
        return second_max
    
    else:

        return third_max





print(third_max([3, 2, 1]))

print(third_max([1, 2]))

print(third_max([2, 2, 3, 1]))

print(third_max([2]))

print(third_max([2, 2, 3, 2, 2]))


'''
if len(nums) >= 3:

        third_max = nums[2]
    else:
        third_max = nums[-1]
        
    return(third_max)
'''