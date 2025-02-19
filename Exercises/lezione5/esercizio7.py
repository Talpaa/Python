def check_parentheses(expression: str) -> bool:
    
    condizione: bool = True    

    par_aper: int = 0
    par_chiu: int = 0

    for i in expression:

        if i == '(':

            par_aper += 1

        elif i == ')':

            par_chiu += 1

        if par_aper < par_chiu:

            return False

    if par_aper != par_chiu:

        condizione = False

    return condizione



print(check_parentheses("()()"))