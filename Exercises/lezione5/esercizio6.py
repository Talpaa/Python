def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    
    operazione: str = ''

    if (conditionA == True)or((conditionB == True)and(conditionC == True)):

        operazione = "Operazione permessa"

    else:

        operazione = "Operazione negata"

    return operazione


print(check_combination(True, False, True))

print(check_combination(False, True, False))