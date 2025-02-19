file_path = 'prova/prova.txt'
f = open(file_path, 'r')

first_row = f.readline()
print(f'La prima riga è {first_row}')

second_row = f.readline()
print(f'La seconda riga è {second_row}')
f.close


with open(file_path, 'w') as f:
    #leggi e fai quello che ti pare col file

    f.write('Bella per te')



with open(file_path, 'a+') as f:
    #leggi e fai quello che ti pare col file

    f.write('\nBella per te')