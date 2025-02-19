def check_combination(a: bool, b: bool, c: bool):

    if (a or (b and c)):

        return f'Operazione permessa'
    
    else:

        return f'Operazione negata'

print(check_combination(True, False, True))#Operazione permessa

print(check_combination(False, True, False))#Operazione negata