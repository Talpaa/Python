import random

def estrazione():

    return random.randrange(0, 15)

numeri: list = [0,1,2,3,4,5,6,7,8,9, 'a', 'b', 'c', 'd','e','f']

extracted_numbers: list = []

extracted_numbers.append(numeri[estrazione()])
extracted_numbers.append(numeri[estrazione()])
extracted_numbers.append(numeri[estrazione()])
extracted_numbers.append(numeri[estrazione()])

golden_ticket: str = f'{extracted_numbers[0]}-{extracted_numbers[1]}-{extracted_numbers[2]}-{extracted_numbers[3]}'

print(f'\n\nTutti i biglietti uguali a questo {golden_ticket.upper()} sono vincitori')