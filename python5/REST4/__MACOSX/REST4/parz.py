import dbclient as db

cur = db.connect()

print('\n\ncosa vuoi fare?\n')
print('     1. query di lettura')
print('     2. query di scrittura')
print('     3. query di modifica')
print('     4. query di eliminazione')
print('     5. EXIT')

ris = input('\nRisposta: ')

while (ris != '5'):

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

    elif ris == '3':

        utente = input('Inserire lo user dell\'utente che si vuole modificare: ')
        
        db.read_in_db(cur, f"select * from utenti where utente = '{utente}';")
        row = db.read_next_row(cur)[1]
        
        print(row)

        if row:

            flag: bool = False

            if (input('Vuoi modificare il nome utente(s/n): ') == 's'):
                user = input('Inserire il nuovo nome utente: ')
                flag = True
            else:
                user = row[0]

            if (input('Vuoi modificare la password(s/n): ') == 's'):    
                password = input('Inserire la nuova password: ')
                flag = True
            else:
                password = row[1]

            if (input('Vuoi modificare il livello di permesso(s/n): ') == 's'):
                privileggi = input('Inserire il nuovo livello di permesso: ')
                flag = True
            else:
                privileggi = row[2]
            
            if (input('Vuoi modificare la descrizione dell\'utente(s/n): ') == 's'):
                note = input('Inserire una nuova descrizione: ')
                flag = True
            else:
                note = row[3]

            if flag:
                print(f'\nUser modificato: {user}\nPassword: {password}\nPrivileggi: {privileggi}\nAnnotazione: {note}')
                
                sQuery = f"UPDATE utenti SET utente = '{user}', password = '{password}', privileggi = '{privileggi}', note = '{note}' WHERE utente = '{utente}';"
                print(sQuery)
                ris = db.write_in_db(cur, sQuery)
            else:
                print(f'\n\nNessuna modifica da effetuare.')

        else:

            print('\nUtente inesistente')

    elif ris == '4':
        
        user = input('Inserire lo user dell\'utente che si vuole eliminare: ')

        db.read_in_db(cur, f"select * from utenti where utente = '{user}';")

        row = db.read_next_row(cur)[1]
        
        print(row)

        if row:

            sQuery = f"DELETE FROM utenti WHERE utente = '{user}';"
            print(sQuery)
            ris = db.write_in_db(cur, sQuery)

            if ris == 0:

                print(f'Utente eliminato')
            
            else:

                print(f'Utente non eliminato')
        else:

            print(f'User inesistente')

    else: 

        print(f'La sceltra {ris} non è valida.')

    print('\n\ncosa vuoi fare?\n')
    print('     1. query di lettura')
    print('     2. query di scrittura')
    print('     3. query di modifica')
    print('     4. query di eliminazione')
    print('     5. EXIT')

    ris = input('\nRisposta: ')
