def is_valid_parenthesis(expression: str) -> bool:
    
    condizione: bool = True   


    par_ton_aper: int = 0
    par_ton_chiu: int = 0
    par_qua_aper: int = 0
    par_qua_chiu: int = 0
    par_gra_aper: int = 0
    par_gra_chiu: int = 0
    


    for i in range(len(expression)):

        if expression[i] == '(':

            par_ton_aper += 1

            if (expression[i+1] == ']')or(expression[i+1] == '}'):
                return False

        elif expression[i] == (')'):

            par_ton_chiu += 1

        elif expression[i] == '[':

            par_qua_aper += 1

            if (expression[i+1] == '}')or(expression[i+1] == ')'):
                return False

        elif expression[i] == ']':

            par_qua_chiu += 1

        elif expression[i] == '{':

            par_gra_aper +=1

            if (expression[i+1] == ']')or(expression[i+1] == ')'):
                return False

        elif expression[i] == '}':

            par_gra_chiu += 1

        if (par_ton_aper < par_ton_chiu)or(par_qua_aper < par_qua_chiu)or(par_gra_aper < par_gra_chiu):

            return False
        

    if (par_ton_aper != par_ton_chiu)or(par_qua_aper != par_qua_chiu)or(par_gra_aper != par_gra_chiu):

        condizione = False

    return condizione
	

print(is_valid_parenthesis("()"))#True

print(is_valid_parenthesis("()[]{}"))#True 

print(is_valid_parenthesis("(]"))#False

print(is_valid_parenthesis("([)]")) #False X

print(is_valid_parenthesis("{[]}"))#True 

print(is_valid_parenthesis(""))#True

'''
(par_ton_aper < par_ton_chiu)or(par_ton_aper < par_qua_chiu)or(par_ton_aper < par_gra_chiu)or\
(par_qua_aper < par_qua_chiu)or(par_qua_aper < par_ton_chiu)or(par_qua_aper < par_gra_chiu)or\
(par_gra_aper < par_gra_chiu)or(par_gra_aper < par_ton_chiu)or(par_gra_aper < par_qua_chiu)
'''