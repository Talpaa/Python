class FormulaError(Exception): 
     pass

def is_float(num: str | int):

    try:

        float(num)
        return True
    
    except ValueError:

        return False
    
def separa_elementi(formula: str):

    lista_elementi: list[str] = formula.split()


    if len(lista_elementi) != 3:
        raise FormulaError('Input does not consist of three elements')
    
    return lista_elementi
    
def calculator():

    risposta: str = 'y'
    formula: str = ''


    while(risposta == 'y'):

        formula = input('inserisci la formula con questo formato \'numero operatore numero\':\n ')

        lista_elementi: list[str] = separa_elementi(formula)

        elemento1: str = lista_elementi[0].replace(',', '.')
        elemento2: str = lista_elementi[1]
        elemento3: str = lista_elementi[2].replace(',', '.')

        risposta1: bool = is_float(elemento1)
        risposta3: bool = is_float(elemento3)

        if (risposta1)and(risposta3):

            elemento1 = float(elemento1)
            elemento3 = float(elemento3)

            if(elemento2 == '+'):

                print(f'{round(elemento1 + elemento3, 3)}')

            elif(elemento2 == '-'):

                print(f'{round(elemento1 - elemento3, 3)}')
            
            elif(elemento2 == '*'):

                print(f'{round(elemento1 * elemento3, 3)}')
            
            elif(elemento2 == '/'):

                if elemento3 == 0:
                        
                    raise FormulaError('the third element cannot be zero')
                        
                else:

                    print(f'{round(elemento1 / elemento3, 3)}')

            else:

                raise FormulaError('The second element is not an arithmetic operator')
            
        elif (not(risposta1))and(not(risposta3)):

            raise FormulaError('The first and third elements are not real numbers.')
        
        elif not(risposta1):

            raise FormulaError('The first element is not a real number')

        elif not(risposta3):

            raise FormulaError('The third element is not a real number')
        
        risposta = input('Vuoi calcolare qualcos\'altro?(y/n): ')


calculator()

