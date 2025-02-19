import random

def estrazione(a: int):

    return random.randrange(0, a)

numeri: list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
my_ticket: list = []

print('\n\nQuesti sono i numeri tra cui puoi scegliere:\n'\
      +'[0-1-2-3-4-5-6-7-8-9-A-B-C-D-E-F]\n'\
        +'ognuno può essere presente una sola volta sul biglietto vincitore\n')

for i in range(1,5):

    inserimento = input('Inserisci uno dei quattro numeri che vuoi giocare: ').upper()

    while not(inserimento in numeri):

        print('\n il numero inserito non è tra quelli da scegliere')
        inserimento = input('Inserisci uno dei quattro numeri che vuoi giocare: ').upper()

    numeri.remove(inserimento)
    my_ticket.append(inserimento)

print(my_ticket)


diversi: list = [True,True,True,True]

conteggio: int = 0

while((diversi[0])or(diversi[1])or(diversi[2])or(diversi[3])):

    conteggio += 1
    numeri: list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']#

    extracted_numbers: list = []

    extracted_numbers.append(numeri[estrazione(len(numeri))])
    numeri.remove(extracted_numbers[0])

    extracted_numbers.append(numeri[estrazione(len(numeri))])
    numeri.remove(extracted_numbers[1])

    extracted_numbers.append(numeri[estrazione(len(numeri))])
    numeri.remove(extracted_numbers[2])

    extracted_numbers.append(numeri[estrazione(len(numeri))])
    numeri.remove(extracted_numbers[3])

    print(extracted_numbers)

    for i in range(0,4):

        for j in range(0,4):

            if extracted_numbers[i] == my_ticket[j]:

                print('F')
                diversi.pop(i)
                diversi.insert(i,False)
                break

            else:

                print('V')
                diversi.pop(i)
                diversi.insert(i,True)


print(f'\n\nHai vinto dopo {conteggio} tentaivi')