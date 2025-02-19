from flask import Flask, json, request
import dbclient as db

#Connessione al DataBase
cur = db.connect()

api = Flask(__name__)

#controlla se chi chiede di comunicare col DB abbia i permessi
def controllo(operatore, operazione):
    
    print(f'operatore: {operatore}')
    print(f'operazione: {operazione}')

    user = operatore['user']
    password = operatore["password"]

    global cur
    #carichiamo gli utenti
    db.read_in_db(cur, f"select * from utenti where utente = '{user}';")

    row = db.read_next_row(cur)[1]

    print(row)

    #controllo esistenza operatore
    if user in row:

        if password == row[1]:
            #carico i permessi
            permesso = row[2]

            if (operazione == 1)and(permesso == 'w'):   return True
            
            elif (operazione == 2)and((permesso == 'w')or(permesso == 'r')):    return True

            elif (operazione == 3)and(permesso == 'w'): return True

            elif (operazione == 4)and(permesso == 'w'): return True
            
            else:   return False
        else:   return False
    else:   return False
@api.route('/registra', methods=['POST'])
def registra():
    global cur 

    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print('Ricevuta chiamata ' + content_type)

    if content_type == 'application/json':

        jRequest = request.json
        user = jRequest["operatore"]['user']
        password = jRequest["operatore"]['password']

        print(f'Operatore: {jRequest["operatore"]}')

        #Prendiamo l'utente dal db
        db.read_in_db(cur, f"select * from utenti u where u.utente = '{user}';")

        row = db.read_next_row(cur)[1]

        print(row)

        #controlla che l'operatore esista
        if user in row:
            
            if password == row[1]:

                if not(row[4]):
                    sQuery = f"UPDATE utenti SET registrazione = 'true' WHERE utente = '{user}';"
                    db.write_in_db(cur, sQuery)
                    jResponse = {'Error': '000', 'msg':'ok', 'user': row} 
                    return json.dumps(jResponse), 200
                else:
                    jResponse = {'Error': '001', 'msg':'Utente già Registrato'} 
                return json.dumps(jResponse), 200
            else:

                jResponse = {'Error': '001', 'msg':'Password Errata'} 
                return json.dumps(jResponse), 200

        else:

            jResponse = {'Error': '001', 'msg':'Utente non esistente'} 
            return json.dumps(jResponse), 200
        
    else:

        return {'Error': '401', 'msg':'formato non riconosciuto'}
    
@api.route('/accedi', methods=['POST'])
def accedi():
    global cur
    
    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print('Ricevuta chiamata ' + content_type)

    if content_type == 'application/json':

        jRequest = request.json
        user = jRequest["operatore"]['user']
        password = jRequest["operatore"]['password']

        print(f'Operatore: {jRequest["operatore"]}')

        #Prendiamo l'utente dal db
        db.read_in_db(cur, f"select * from utenti u where u.utente = '{user}';")

        row = db.read_next_row(cur)[1]

        print(row)

        #controlla che l'operatore esista
        if user in row:
            
            if password == row[1]:

                if row[4]:
                    jResponse = {'Error': '000', 'msg':'ok', 'user': row} 
                    return json.dumps(jResponse), 200
                else:
                    jResponse = {'Error': '001', 'msg':'not ok'} 
                    return json.dumps(jResponse), 200
            else:

                jResponse = {'Error': '001', 'msg':'Password Errata'} 
                return json.dumps(jResponse), 200

        else:

            jResponse = {'Error': '001', 'msg':'Utente non esistente'} 
            return json.dumps(jResponse), 200
        
    else:

        return {'Error': '401', 'msg':'formato non riconosciuto'}

    

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    global cur

    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print('Ricevuta chiamata ' + content_type)

    if content_type == 'application/json':

        #Dati cittadino e operatore
        jRequest = request.json
        sCodiceFiscale = jRequest["cittadino"]['codiceFiscale']
        sNome = jRequest["cittadino"]['nome']
        sCognome = jRequest["cittadino"]['cognome']
        sData = jRequest["cittadino"]['dataNascita']
        print(jRequest)


        #carichiamo l'anagrafe
        db.read_in_db(cur, f"select * from cittadini where codice_fiscale = '{sCodiceFiscale}';")

        row = db.read_next_row(cur)[1]

        print(row)
        
        #controlla che il cittadino non sia già presente
        if row == None:

            sQuery = f"INSERT INTO cittadini VALUES ('{sCodiceFiscale}', '{sNome}', '{sCognome}', to_date('{sData}', 'YYYY-MM-DD')); "
            print(sQuery)
            ris = db.write_in_db(cur, sQuery)

            if ris == 0:

                sQuery = f"select * from cittadini where codice_fiscale = '{sCodiceFiscale}';"
                print(db.read_in_db(cur, sQuery))

                row = db.read_next_row(cur)[1]

                jResponse = {'Error': "000", 'info': row, 'msg':'ok'} 
                return json.dumps(jResponse), 200
            
            else:

                jResponse = {'Error': f'{ris}', 'msg':'ko'} 
                return json.dumps(jResponse), 200
        else:

            jResponse = {'Error': '001', 'msg':'Codice Fiscale già presente'} 
            return json.dumps(jResponse), 200
    else:

        return 'Errore, formato non riconosciuto', 401
    

@api.route('/info_cittadino', methods=['POST'])
def GestisciInfoCittadino():
    global cur
    
    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print('Ricevuta chiamata ' + content_type)

    if content_type == 'application/json':

        #Dati cittadino e operatore
        jRequest = request.json
        sCodiceFiscale = jRequest["user"]
        print(jRequest)

        

        #carichiamo l'anagrafe
        print(db.read_in_db(cur, f"select * from cittadini where codice_fiscale = '{sCodiceFiscale}';"))

        row = db.read_next_row(cur)[1]
        print(row)

        if row:

            jResponse = {'Error': '000', 'msg':'ok', 'info': row} 
            return json.dumps(jResponse), 200
        else:

            jResponse = {'Error': '001', 'msg':'Codice Fiscale non presente'} 
            return json.dumps(jResponse), 200
    else:

        return 'Errore, formato non riconosciuto', 401

@api.route('/modifica_cittadino', methods=['POST'])
def ModificaCittadino():
    global cur
    
    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print('Ricevuta chiamata ' + content_type)

    if content_type == 'application/json':

        #Dati cittadino e operatore
        jRequest = request.json
        sCodiceFiscale = jRequest["cittadino"]['codiceFiscale']
        modifiche = jRequest['modifiche']
        print(jRequest)

        #carichiamo l'anagrafe
        #dAnagrafe = JsonDeserialize(sFileAnagrafe)

        db.read_in_db(cur, f"select * from cittadini c where c.codice_fiscale = '{sCodiceFiscale}';")

        row = db.read_next_row(cur)[1]

        print(row)
        print(modifiche)
        if row:

            persona = list(row)

            test: bool = False
            n = 0
            
            for key in modifiche:
                if modifiche[key] != '':

                    test = True
                    persona[n] = modifiche[key]
                n += 1
            
            if test:

                cf = persona[0]
                nome = persona[1]
                cognome = persona[2]
                data = persona[3]
                
                print(cf)
                print(nome)
                print(data)
                print(cognome)                

                sQuery = f"UPDATE cittadini SET codice_fiscale = '{cf}', nome = '{nome}', cognome = '{cognome}', data_nascita = to_date('{data}', 'YYYY-MM-DD') WHERE codice_fiscale = '{sCodiceFiscale}';"
                print(sQuery)
                ris = db.write_in_db(cur, sQuery)

                if ris == 0:

                    jResponse = {'Error': f'{ris}', 'msg':'modifiche effettuate', 'info': persona} 
                    return json.dumps(jResponse), 200
                
                else:

                    jResponse = {'Error': f'{ris}', 'msg':'modifiche andate male'} 
                    return json.dumps(jResponse), 200

            else:
                jResponse = {'Error': '000', 'msg':'nessuna modifica effettuata'} 
                return json.dumps(jResponse), 200
        else:

            jResponse = {'Error': '001', 'msg':'Codice Fiscale non presente'} 
            return json.dumps(jResponse), 200
            
    else:

        return 'Errore, formato non riconosciuto', 401
    

@api.route('/elimina_cittadino', methods=['POST'])
def EliminaCittadino():
    global cur
    
    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print('Ricevuta chiamata ' + content_type)

    if content_type == 'application/json':

        #Dati cittadino e operatore
        jRequest = request.json
        sCodiceFiscale = jRequest["cittadino"]['codiceFiscale']
        print(jRequest)

        #carichiamo l'anagrafe
        db.read_in_db(cur, f"select * from cittadini c where c.codice_fiscale = '{sCodiceFiscale}';")

        row = db.read_next_row(cur)[1]
        
        print(row)

        if row:

            sQuery = f"DELETE FROM cittadini WHERE codice_fiscale = '{sCodiceFiscale}';"
            print(sQuery)
            ris = db.write_in_db(cur, sQuery)

            if ris == 0:

                jResponse = {'Error': f'{ris}', 'info': row, 'msg':'Cittadino eliminato'} 
                return json.dumps(jResponse), 200
            
            else:

                jResponse = {'Error': f'{ris}', 'msg':'Cittadino non eliminato'} 
                return json.dumps(jResponse), 200
        else:

            jResponse = {'Error': '001', 'msg':'Codice Fiscale non presente'} 
            return json.dumps(jResponse), 200
    else:

        return 'Errore, formato non riconosciuto', 401

api.run(host='127.0.0.1', port=8080, ssl_context='adhoc')