import json, requests

base_url = 'https://127.0.0.1:8080'

def RIchiediDatiCittadino(user, password):

    nome: str = input('Inserisci il nome del cittadino: ')
    cognome: str = input('Inserisci il cognome del cittadino: ')
    data: str = input('Inserisci la data di nascita del cittadino: ')
    cf: str = input('Inserisci il codice fiscale del cittadino: ')

    jRequest = {"cittadino":{'nome':nome, 'cognome':cognome, 'dataNascita':data,'codiceFiscale': cf}, "operatore":{'user': user, 'password': password}}
    return jRequest

def InvioCodiceFiscale(user, password):
    
    codiceFiscale: str = input('Inserisci il codice fiscale del cittadino: ')

    jRequest = {"cittadino":{'codiceFiscale': codiceFiscale}, "operatore":{'user': user, 'password': password}}
    return jRequest

def ModificaDatiCittadino(user, password):
    
    codiceFiscale: str = input('Inserisci il codice fiscale del cittadino: ')

    ris = input('Vuoi cambiare il codice fiscale:(s/n) ')
    if ris == 's':

        cf = input('Inserire il nuovo codice fiscale: ')
    else:

        cf = 0

    ris = input('Vuoi cambiare il nome:(s/n) ')
    if ris == 's':

        nome = input('Inserire il nuovo nome: ')
    else:

        nome = 0

    ris = input('Vuoi cambiare il cognome:(s/n) ')
    if ris == 's':

        cognome = input('Inserire il nuovo cognome: ')
    else:

        cognome = 0

    ris = input('Vuoi cambiare la data di nascita:(s/n) ')
    if ris == 's':

        data = input('Inserire la data di nascita: ')
    else:

        data = 0

    jRequest = {'codiceFiscale': codiceFiscale, 'modifiche':{'codiceFiscale':cf, 'nome':nome, 'cognome':cognome, 'dataNascita':data}, "operatore":{'user': user, 'password': password}}
    return jRequest

def EliminaDatiCittadino(user, password):
    
    codiceFiscale: str = input('Inserisci il codice fiscale del cittadino: ')

    jRequest = {"cittadino":{'codiceFiscale': codiceFiscale}, "operatore":{'user': user, 'password': password}}
    return jRequest

def CreaInterfaccia(permesso):

    print()
    print('        Operazioni disponibili')

    if(permesso == 'w'):
        print()
        print('1. Inserisci cittadino (es. atto di nascita)')
        print('2. Richiedi dati cittadino (es. cert. residenza)')
        print('3. Modifica dati cittadino')
        print('4. Elimina cittadino')
        print('5. Exit')
    
    elif(permesso == 'r'):
        
        print()
        print('2. Richiedi dati cittadino (es. cert. residenza)')
        print('5. Exit')

    else:
        
        print()
        print('5. Exit')

def accedi():
    
    print()
    user: str = input('Inserisci l\'email di login: ')
    print()
    password: str = input('Inserisci password: ')

    jRequest = {"operatore":{'user': user, 'password': password}}
    return jRequest


login = False

while login == False:

    api_url = base_url + '/accedi'
    jsonDataRequest = accedi()

    try:

        response = requests.post(api_url,json=jsonDataRequest,verify=False)
        print()
        print(response.status_code)
        print(response.headers["Content-Type"])
        data1 = response.json()
        print(data1)
    except:
        print('Problemi di connessione con il server, riprova più tardi')

    if data1['msg'] == 'ok':

        login = True
        user: str = jsonDataRequest["operatore"]['user']
        password: str = data1['user']['password']
        permesso: str = data1['user']['privileggi']
        note: str = data1['user']['note']

if login:
    CreaInterfaccia(permesso)
    print()
    sOper = input('Selezione operazione: ')

    while (sOper != '5'):    

        if sOper == '1':
            
            if permesso == 'w':

                api_url = base_url + '/add_cittadino'
                jsonDataRequest = RIchiediDatiCittadino(user, password)

                try:

                    response = requests.post(api_url,json=jsonDataRequest,verify=False)
                    print()
                    print(response.status_code)
                    print(response.headers["Content-Type"])
                    data1 = response.json()
                    print(data1)
                except:
                    print('Problemi di connessione con il server, riprova più tardi')
            else:

                print('Permesso negato')
        elif sOper == '2':

            if(permesso == 'r')or(permesso == 'w'):

                api_url = base_url + '/info_cittadino'
                jsonDataRequest = InvioCodiceFiscale(user, password)
            
                res = True

                try:

                    response = requests.post(api_url,json=jsonDataRequest,verify=False)
                    print()
                    print(response.status_code)
                    print(response.headers["Content-Type"])
                    
                    data1 = response.json()

                    res = False
                
                    info = data1.pop('info')
                    nome = info["nome"]
                    cognome = info["cognome"]
                    data = info["dataNascita"]
                    codfis = info["codiceFiscale"]

                    print(data1)
                    print()
                    print(f'NOME: {nome}')
                    print(f'COGNOME: {cognome}')
                    print(f'DATA DI NASCITA: {data}')
                    print(f'CODICE FISCALE: {codfis}')


                except:

                    if res:
                        print('Problemi di connessione con il server, riprova più tardi')
                    else:
                        print(data1)
            else:

                print('Permesso Negato')
        elif sOper == '3':
            

            if permesso == 'w':

                api_url = base_url + '/modifica_cittadino'
                jsonDataRequest = ModificaDatiCittadino(user, password)

                try:

                    response = requests.post(api_url,json=jsonDataRequest,verify=False)
                    print()
                    print(response.status_code)
                    print(response.headers["Content-Type"])
                    
                    data1 = response.json()
                    
                    print(data1)
                    print()


                except:
                    print('Problemi di connessione con il server, riprova più tardi')

            else:

                print('Permesso Negato')

        elif sOper == '4':
            
            if permesso == 'w':
                
                api_url = base_url + '/elimina_cittadino'
                jsonDataRequest = EliminaDatiCittadino(user, password)

                try:

                    response = requests.post(api_url,json=jsonDataRequest,verify=False)
                    print()
                    print(response.status_code)
                    print(response.headers["Content-Type"])
                    
                    data1 = response.json()
                    
                    print(data1)
                    print()


                except:
                    print('Problemi di connessione con il server, riprova più tardi')
            
            else:

                print('Permesso Negato')

        else:
            
            print('Operazione inesistente')
        
        CreaInterfaccia(permesso)
        print()
        sOper = input('Selezione operazione: ')