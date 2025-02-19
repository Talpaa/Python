from flask import Flask, json, request

import dbclient as db

cur = db.connect()
api = Flask(__name__)

def controllo(operatore, operazione):
    
    global cur
    #carichiamo gli utenti
    db.read_in_db(cur, f"select * from utenti where utente = '{operatore['user']}';")

    row = db.read_next_row(cur)[1]

    #controllo esistenza operatore
    if row:

        if operatore["password"] == row[1]:
            #carico i permessi
            permesso = row[2]

            if (operazione == 1)and(permesso == 'w'):
                
                return True, row[3]
            
            elif (operazione == 2)and(permesso == 'r'):
                
                return True, row[3]

            else:

                return False
        else:

            return False
    else:

        return False
    
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
        if row:
            
            if password == row[1]:

                jResponse = {'Error': '000', 'msg':'ok', 'user': row} 
                return json.dumps(jResponse), 200
            
            else:

                jResponse = {'Error': '001', 'msg':'Password Errata'} 
                return json.dumps(jResponse), 200

        else:

            jResponse = {'Error': '001', 'msg':'Utente non trovato'} 
            return json.dumps(jResponse), 200
        
    else:

        return 'Errore, formato non riconosciuto', 401

    

@api.route('/add_casa_vendita', methods=['POST'])
def GestisciAddCasaVendità():
    global cur

    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print('Ricevuta chiamata ' + content_type)

    if content_type == 'application/json':

        #Dati cittadino e operatore
        jRequest = request.json
        
        sCatastale = jRequest["casa"]['catastale']
        sIndirizzo = jRequest["casa"]['indirizzo']
        sCivico = jRequest["casa"]['civico']
        sPiano = jRequest["casa"]['piano']
        sMetri = jRequest["casa"]['metri']
        sStanze = jRequest["casa"]['stanze']
        sPrezzo = jRequest["casa"]['prezzo']
        sStato = jRequest["casa"]['stato']
        print(jRequest)

        operatore = jRequest["operatore"]

        con = controllo(operatore, 1)

        if con[0]:

            #carichiamo l'anagrafe
            db.read_in_db(cur, f"select * from case_in_vendita where catastale = '{sCatastale}';")

            row = db.read_next_row(cur)[1]
            
            #controlla che il cittadino non sia già presente
            if row == None:

                sQuery = f"INSERT INTO case_in_vendita VALUES ('{sCatastale}', '{sIndirizzo}', '{sCivico}', '{sPiano}', '{sMetri}', '{sStanze}', '{sPrezzo}', '{sStato}', '{con[1]}'); "
                print(sQuery)
                ris = db.write_in_db(cur, sQuery)

                if ris == 0:

                    jResponse = {'Error': f'{ris}', 'msg':'ok'} 
                    return json.dumps(jResponse), 200
                
                else:

                    jResponse = {'Error': f'{ris}', 'msg':'ko'} 
                    return json.dumps(jResponse), 200
            else:

                jResponse = {'Error': '001', 'msg':'Codice Fiscale già presente'} 
                return json.dumps(jResponse), 200
        else:

            jResponse = {'Error': '001', 'msg':'Permesso Negato'} 
            return json.dumps(jResponse), 200
    else:

        return 'Errore, formato non riconosciuto', 401
    
@api.route('/add_casa_affitto', methods=['POST'])
def GestisciAddCasaAffitto():
    global cur

    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print('Ricevuta chiamata ' + content_type)

    if content_type == 'application/json':

        #Dati cittadino e operatore
        jRequest = request.json
        
        sCatastale = jRequest["casa"]['catastale']
        sIndirizzo = jRequest["casa"]['indirizzo']
        sCivico = jRequest["casa"]['civico']
        sPrezzo = jRequest["casa"]['prezzo']
        sAffitto = jRequest["casa"]['affitto']
        sBagno = jRequest["casa"]['bagno']
        print(jRequest)

        operatore = jRequest["operatore"]

        con = controllo(operatore, 1)

        if con[0]:

            #carichiamo l'anagrafe
            db.read_in_db(cur, f"select * from case_in_affitto where catastale = '{sCatastale}';")

            row = db.read_next_row(cur)[1]
            
            #controlla che il cittadino non sia già presente
            if row == None:

                sQuery = f"INSERT INTO case_in_affitto VALUES ('{sCatastale}', '{sIndirizzo}', '{sCivico}', '{sAffitto}', '{sBagno}', '{sPrezzo}', '{con[1]}'); "
                print(sQuery)
                ris = db.write_in_db(cur, sQuery)

                if ris == 0:

                    jResponse = {'Error': f'{ris}', 'msg':'ok'} 
                    return json.dumps(jResponse), 200
                
                else:

                    jResponse = {'Error': f'{ris}', 'msg':'ko'} 
                    return json.dumps(jResponse), 200
            else:

                jResponse = {'Error': '001', 'msg':'Codice Fiscale già presente'} 
                return json.dumps(jResponse), 200
        else:

            jResponse = {'Error': '001', 'msg':'Permesso Negato'} 
            return json.dumps(jResponse), 200
    else:

        return 'Errore, formato non riconosciuto', 401
    

@api.route('/elimina_casa_vendita', methods=['POST'])
def EliminaCasaVendita():
    global cur
    
    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print('Ricevuta chiamata ' + content_type)

    if content_type == 'application/json':

        #Dati cittadino e operatore
        jRequest = request.json
        sCatastale = jRequest["casa"]['catastale']
        print(jRequest)

        operatore = jRequest["operatore"]

        con = controllo(operatore, 1)

        if con[0]:

            #carichiamo l'anagrafe
            db.read_in_db(cur, f"select * from case_in_vendita where catastale = '{sCatastale}';")

            row = db.read_next_row(cur)[1]
            
            print(sCatastale)
            print(row)

            if sCatastale in row:

                sQuery = f"DELETE FROM case_in_vendita WHERE catastale = '{sCatastale}';"
                print(sQuery)
                ris = db.write_in_db(cur, sQuery)

                if ris == 0:

                    jResponse = {'Error': f'{ris}', 'msg':'Casa eliminata'} 
                    return json.dumps(jResponse), 200
                
                else:

                    jResponse = {'Error': f'{ris}', 'msg':'Casa non eliminata'} 
                    return json.dumps(jResponse), 200
            else:

                jResponse = {'Error': '001', 'msg':'Codice Catastale non presente'} 
                return json.dumps(jResponse), 200
        else:
            jResponse = {'Error': '001', 'msg':'Permesso Negato'} 
            return json.dumps(jResponse), 200
    else:

        return 'Errore, formato non riconosciuto', 401
    
@api.route('/elimina_casa_affitto', methods=['POST'])
def EliminaCasaAffitto():
    global cur
    
    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print('Ricevuta chiamata ' + content_type)

    if content_type == 'application/json':

        #Dati cittadino e operatore
        jRequest = request.json
        sCatastale = jRequest["casa"]['catastale']
        print(jRequest)

        operatore = jRequest["operatore"]

        con = controllo(operatore, 1)

        if con[0]:

            #carichiamo l'anagrafe
            db.read_in_db(cur, f"select * from case_in_affitto where catastale = '{sCatastale}';")

            row = db.read_next_row(cur)[1]
            
            print(sCatastale)
            print(row)

            if sCatastale in row:

                sQuery = f"DELETE FROM case_in_affitto WHERE catastale = '{sCatastale}';"
                print(sQuery)
                ris = db.write_in_db(cur, sQuery)

                if ris == 0:

                    jResponse = {'Error': f'{ris}', 'msg':'Casa eliminata'} 
                    return json.dumps(jResponse), 200
                
                else:

                    jResponse = {'Error': f'{ris}', 'msg':'Casa non eliminata'} 
                    return json.dumps(jResponse), 200
            else:

                jResponse = {'Error': '001', 'msg':'Codice Catastale non presente'} 
                return json.dumps(jResponse), 200
        else:
            jResponse = {'Error': '001', 'msg':'Permesso Negato'} 
            return json.dumps(jResponse), 200
    else:

        return 'Errore, formato non riconosciuto', 401


@api.route('/cerca_casa_vendita', methods=['POST'])
def CercaCasaVendita():
    global cur
    
    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print('Ricevuta chiamata ' + content_type)

    if content_type == 'application/json':

        #Dati cittadino e operatore
        jRequest = request.json
        
        print(jRequest)

        operatore = jRequest["operatore"]

        con = controllo(operatore, 1)

        if con[0]:

            casa = jRequest['casa']
            sVar = casa[0]
            sVal = casa[1]

            if (len(casa) == 3):

                sValMin = casa[2] 
                db.read_in_db(cur, f"select * from case_in_vendita where {sVar} <= '{sVal}' and {sVar} >= '{sValMin}';")

            elif (len(casa) == 4):
                
                sVar2 = casa[2]
                sVal2 = casa[3] 
                db.read_in_db(cur, f"select * from case_in_vendita where {sVar} = '{sVal}' and {sVar2} = '{sVal2}';")

            else:
                
                db.read_in_db(cur, f"select * from case_in_vendita where {sVar} = '{sVal}';")
                print()

            rows = db.read_all_row(cur)[1]

            print(rows)
            
            if rows:

                rows = list(rows)

                jResponse = {'Error': '000', 'msg': rows} 
                return json.dumps(jResponse), 200
            
            else:

                jResponse = {'Error': '001', 'msg':'Nessuna casa con queste caratteristiche'} 
                return json.dumps(jResponse), 200
        else:
            jResponse = {'Error': '001', 'msg':'Permesso Negato'} 
            return json.dumps(jResponse), 200
    else:

        return 'Errore, formato non riconosciuto', 401
    
@api.route('/cerca_casa_affitto', methods=['POST'])
def CercaCasaAffitto():
    global cur
    
    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print('Ricevuta chiamata ' + content_type)

    if content_type == 'application/json':

        #Dati cittadino e operatore
        jRequest = request.json
        
        print(jRequest)

        operatore = jRequest["operatore"]

        con = controllo(operatore, 1)

        if con[0]:

            casa = jRequest['casa']
            sVar = casa[0]
            sVal = casa[1]

            if (len(casa) == 3):

                sValMin = casa[2] 
                db.read_in_db(cur, f"select * from case_in_affitto where {sVar} <= '{sVal}' and {sVar} >= '{sValMin}';")

            elif (len(casa) == 4):
                
                sVar2 = casa[2]
                sVal2 = casa[3] 
                db.read_in_db(cur, f"select * from case_in_affitto where {sVar} = '{sVal}' and {sVar2} = '{sVal2}';")

            else:
                
                db.read_in_db(cur, f"select * from case_in_affitto where {sVar} = '{sVal}';")
                print()

            rows = db.read_all_row(cur)[1]

            print(rows)
            
            if rows:

                rows = list(rows)

                jResponse = {'Error': '000', 'msg': rows} 
                return json.dumps(jResponse), 200
            
            else:

                jResponse = {'Error': '001', 'msg':'Nessuna casa con queste caratteristiche'} 
                return json.dumps(jResponse), 200
        else:
            jResponse = {'Error': '001', 'msg':'Permesso Negato'} 
            return json.dumps(jResponse), 200
    else:

        return 'Errore, formato non riconosciuto', 401
    

@api.route('/vendi_casa', methods=['POST'])
def VendiCasa():
    global cur
    
    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print('Ricevuta chiamata ' + content_type)

    if content_type == 'application/json':

        #Dati cittadino e operatore
        jRequest = request.json
        sCatastale = jRequest["casa"]['catastale']
        print(jRequest)

        operatore = jRequest["operatore"]

        con = controllo(operatore, 1)

        if con[0]:

            #carichiamo l'anagrafe
            db.read_in_db(cur, f"select * from case_in_vendita where catastale = '{sCatastale}';")

            casa = db.read_next_row(cur)[1]
            
            print(sCatastale)
            print(casa)

            if sCatastale == casa[0]:

                db.read_in_db(cur, f"select * from vendite_case where catastale = '{sCatastale}';")

                row = db.read_next_row(cur)[1]
            
                print(row)

                if row == None:

                    fil_prop = casa[8]

                    fil_vend = operatore['filiale']
                    prezzo = casa[6]

                    sQuery = 'INSERT INTO vendite_casa(catastale, data_vendita, filiale_proponente, filiale_venditrice, prezzo_vendita)\n'
                    sQuery = sQuery + f'VALUES (\'{sCatastale}\', CURRENT_DATE, \'{fil_prop}\', \'{fil_vend}\', {prezzo});'
                    print(sQuery)
                    ris = db.write_in_db(cur, sQuery)

                    print(ris)

                    if (ris == 0):
                        sQuery = f"DELETE FROM case_in_vendita WHERE catastale = '{sCatastale}';"
                        print(sQuery)
                        ris = db.write_in_db(cur, sQuery)

                        if ris == 0:

                            jResponse = {'Error': f'{ris}', 'msg':'Casa venduta'} 
                            return json.dumps(jResponse), 200
                        
                        else:

                            db.write_in_db(cur, 'ROLLBACK;')

                            jResponse = {'Error': f'{ris}', 'msg':'Casa non venduta'} 
                            return json.dumps(jResponse), 200
                    
                    else:

                        sQuery = f"DELETE FROM case_in_vendita WHERE catastale = '{sCatastale}';"
                        print(sQuery)
                        ris = db.write_in_db(cur, sQuery)

                        jResponse = {'Error': f'{ris}', 'msg':'Casa già venduta'} 
                        return json.dumps(jResponse), 200
                else:

                    sQuery = f"DELETE FROM case_in_vendita WHERE catastale = '{sCatastale}';"
                    print(sQuery)
                    ris = db.write_in_db(cur, sQuery)

                    jResponse = {'Error': '001', 'msg':'Casa già venduta'} 
                    return json.dumps(jResponse), 200

            else:

                jResponse = {'Error': '001', 'msg':'Codice Catastale non presente'} 
                return json.dumps(jResponse), 200
        else:
            jResponse = {'Error': '001', 'msg':'Permesso Negato'} 
            return json.dumps(jResponse), 200
    else:

        return 'Errore, formato non riconosciuto', 401

api.run(host='127.0.0.1', port=8080, ssl_context='adhoc')