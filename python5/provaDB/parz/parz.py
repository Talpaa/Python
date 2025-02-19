import dbclient as db

cur = db.connect()

print('\n\ncosa vuoi fare?\n')
print('     1. query di lettura')
print('     2. query di scrittura')
print('     3. EXIT')

ris = input('\nRisposta: ')

while (ris is not '3'):

    if ris == '1':
        user = input('Inserire lo user dell\'utente che si vuole cercare: ')
        db.read_in_db(cur, f"select * from utenti where utente = '{user}';")
        row = db.read_next_row(cur)[1]
        
        if row:

            print(f'\nUser: {row[0]}\nPassword: {row[1]}\nPrivileggi: {row[2]}\nAnnotazione: {row[3]}')

        else:

            print('\nUtente inesistente')

    elif ris == '2':
        
        user = input('Inserire lo user dell\'utente che si vuole aggiungere: ')
        password = input('Inserire la password dell\'utente che si vuole aggiungere: ')
        privileggi = input('Inserire i privileggi dell\'utente che si vuole aggiungere(UN CARATTERE): ')
        nota = input('Inserire una mini descrizione dell\'utente che si vuole aggiungere(NON OBBLIGATORIO): ')

        ris = db.write_in_db(cur, f"INSERT INTO utenti(utente, password, privileggi, note) VALUES ('{user}', '{password}', '{privileggi}', '{nota}');")

        if ris == 0:

            print(f'\nUtente inserito correttamente.')
        
        else:

            print(f'Lo user \'{user}\' è già in utilizzo.')

    else: 

        print(f'La sceltra {ris} non è valida.')

    print('\n\ncosa vuoi fare?\n')
    print('     1. query di lettura')
    print('     2. query di scrittura')
    print('     3. EXIT')

    ris = input('\nRisposta: ')
