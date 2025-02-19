from flask import Flask, json, request
from myjson import JsonSerialize, JsonDeserialize

sFileAnagrafe = './anagrafe.json'
sFileUtenti = './utenti.json'
api = Flask(__name__)

def controllo(operatore, operazione):
    
    #carichiamo gli utenti
    users = JsonDeserialize(sFileUtenti)

    #controllo esistenza operatore
    if operatore["user"] in users:

        if operatore["password"] == users[operatore["user"]]["password"]:
            #carico i permessi
            permesso = users[operatore["user"]]["privileggi"]

            if (operazione == 1)and(permesso == 'w'):
                
                return True
            
            elif (operazione == 2)and((permesso == 'w')or(permesso == 'r')):
                
                return True

            elif (operazione == 3)and(permesso == 'w'):
                
                return True

            elif (operazione == 4)and(permesso == 'w'):
                
                return True

            else:

                return False
        else:

            return False
    else:

        return False
@api.route('/accedi', methods=['POST'])
def accedi():

    
    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print('Ricevuta chiamata ' + content_type)

    if content_type == 'application/json':

        jRequest = request.json
        user = jRequest["operatore"]['user']
        password = jRequest["operatore"]['password']

        print(jRequest)

        #carichiamo gli utenti
        users = JsonDeserialize(sFileUtenti)

        #controlla che l'operatore esista
        if user in users:
            
            #users[user] = jRequest

            if password == users[user]['password']:

                jResponse = {'Error': '000', 'msg':'ok', 'user': users[user]} 
                return json.dumps(jResponse), 200
            
            else:

                jResponse = {'Error': '001', 'msg':'Password Errata'} 
                return json.dumps(jResponse), 200

        else:

            jResponse = {'Error': '001', 'msg':'Utente non esistente'} 
            return json.dumps(jResponse), 200
        
    else:

        return 'Errore, formato non riconosciuto', 401

    

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():

    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print('Ricevuta chiamata ' + content_type)

    if content_type == 'application/json':

        #Dati cittadino e operatore
        jRequest = request.json
        sCodiceFiscale = jRequest["cittadino"]['codiceFiscale']
        print(jRequest)

        operatore = jRequest["operatore"]

        con = controllo(operatore, 1)

        if con:

            #carichiamo l'anagrafe
            dAnagrafe = JsonDeserialize(sFileAnagrafe)

            #controlla che il cittadino non sia già presente
            if sCodiceFiscale not in dAnagrafe:

                dAnagrafe[sCodiceFiscale] = jRequest["cittadino"]
                JsonSerialize(dAnagrafe, sFileAnagrafe)
                jResponse = {'Error': '000', 'msg':'ok'} 
                return json.dumps(jResponse), 200
            else:

                jResponse = {'Error': '001', 'msg':'Codice Fiscale già presente'} 
                return json.dumps(jResponse), 200
        else:

            jResponse = {'Error': '001', 'msg':'Permesso Negato'} 
            return json.dumps(jResponse), 200
    else:

        return 'Errore, formato non riconosciuto', 401
    

@api.route('/info_cittadino', methods=['POST'])
def GestisciInfoCittadino():
    
    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print('Ricevuta chiamata ' + content_type)

    if content_type == 'application/json':

        #Dati cittadino e operatore
        jRequest = request.json
        sCodiceFiscale = jRequest["cittadino"]['codiceFiscale']
        print(jRequest)

        operatore = jRequest["operatore"]

        con = controllo(operatore, 2)

        if con:

            #carichiamo l'anagrafe
            dAnagrafe = JsonDeserialize(sFileAnagrafe)

            if sCodiceFiscale in dAnagrafe:

                info = dAnagrafe[sCodiceFiscale]
                print(info)
                jResponse = {'Error': '000', 'msg':'ok', 'info': info} 
                return json.dumps(jResponse), 200
            else:

                jResponse = {'Error': '001', 'msg':'Codice Fiscale non presente'} 
                return json.dumps(jResponse), 200
        else:

            jResponse = {'Error': '001', 'msg':'Permesso Negato'} 
            return json.dumps(jResponse), 200
    else:

        return 'Errore, formato non riconosciuto', 401

@api.route('/modifica_cittadino', methods=['POST'])
def ModificaCittadino():
    
    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print('Ricevuta chiamata ' + content_type)

    if content_type == 'application/json':

        #Dati cittadino e operatore
        jRequest = request.json
        sCodiceFiscale = jRequest['codiceFiscale']
        modifiche = jRequest['modifiche']
        print(jRequest)

        operatore = jRequest["operatore"]

        con = controllo(operatore, 3)

        if con:

            #carichiamo l'anagrafe
            dAnagrafe = JsonDeserialize(sFileAnagrafe)

            if sCodiceFiscale in dAnagrafe:

                persona = dAnagrafe[sCodiceFiscale]
                print(persona)

                test: bool = False
                for key in modifiche:

                    if modifiche[key] != 0:

                        test = True
                        persona[key] = modifiche[key]

                if test:

                    dAnagrafe.pop(sCodiceFiscale)
                    dAnagrafe[persona['codiceFiscale']] = persona
                    JsonSerialize(dAnagrafe, sFileAnagrafe)

                    jResponse = {'Error': '000', 'msg':'modifiche effettuate'} 
                    return json.dumps(jResponse), 200
                else:
                    jResponse = {'Error': '000', 'msg':'nessuna modifica effettuata'} 
                    return json.dumps(jResponse), 200
            else:

                jResponse = {'Error': '001', 'msg':'Codice Fiscale non presente'} 
                return json.dumps(jResponse), 200
        else:

            jResponse = {'Error': '001', 'msg':'Permesso Negato'} 
            return json.dumps(jResponse), 200
            
    else:

        return 'Errore, formato non riconosciuto', 401
    

@api.route('/elimina_cittadino', methods=['POST'])
def EliminaCittadino():
    
    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print('Ricevuta chiamata ' + content_type)

    if content_type == 'application/json':

        #Dati cittadino e operatore
        jRequest = request.json
        sCodiceFiscale = jRequest["cittadino"]['codiceFiscale']
        print(jRequest)

        operatore = jRequest["operatore"]

        con = controllo(operatore, 4)

        if con:

            #carichiamo l'anagrafe
            dAnagrafe = JsonDeserialize(sFileAnagrafe)

            if sCodiceFiscale in dAnagrafe:

                persona = dAnagrafe.pop(sCodiceFiscale)
                print(persona)
                JsonSerialize(dAnagrafe, sFileAnagrafe)

                

                jResponse = {'Error': '000', 'msg':'Cittadino eliminato'} 
                return json.dumps(jResponse), 200
            else:

                jResponse = {'Error': '001', 'msg':'Codice Fiscale non presente'} 
                return json.dumps(jResponse), 200
        else:
            jResponse = {'Error': '001', 'msg':'Permesso Negato'} 
            return json.dumps(jResponse), 200
    else:

        return 'Errore, formato non riconosciuto', 401

api.run(host='127.0.0.1', port=8080, ssl_context='adhoc')