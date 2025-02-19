import json, requests

base_url = 'https://127.0.0.1:8080'

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return True
    else:
        return not(float(n).is_integer())

def Data():

    anno: str = input('Inserisci l\'anno di nascita del cittadino: ')
    con = True

    while con:

        try:
            if len(anno) == 4:
                _ = int(anno)
                con = False
            else:
                anno: str = input('Inserisci l\'anno di nascita del cittadino: ')
        except:

            anno: str = input('Inserisci l\'anno di nascita del cittadino: ')
            
    mese: str = input('Inserisci il mese di nascita del cittadino: ')
    con = True

    while con:

        try:
            if len(mese) == 2:
                test = int(mese)
                con = False
            elif len(mese) == 1:
                test = int(mese)
                con = False
                mese = f"0{mese}"
            else:
                mese: str = input('Inserisci il mese di nascita del cittadino: ')

            if (test > 12) or (test < 1):

                con = True
                mese: str = input('Inserisci il mese di nascita del cittadino: ')
        except:

            mese: str = input('Inserisci il mese di nascita del cittadino: ')


    giorno: str = input('Inserisci il giorno di nascita del cittadino: ')
    con = True

    while con:

        try:
            if len(giorno) == 2:
                test = int(giorno)
                con = False
            elif len(giorno) == 1:
                test = int(giorno)
                con = False
                giorno = f"0{giorno}"
            else:
                giorno: str = input('Inserisci il giorno di nascita del cittadino: ')

            if (test > 31) or (test < 1):

                con = True
                giorno: str = input('Inserisci il giorno di nascita del cittadino: ')
        except:

            giorno: str = input('Inserisci il giorno di nascita del cittadino: ')        

    data = f"{anno}-{mese}-{giorno}"

    return data

def RichiediDatiCasa(user, password, scelta):

    catastale: str = input('Inserisci il codice catastale della casa: ')
    indirizzo: str = input('Inserisci il nome della via della casa: ')
    civico: str = input('Inserisci il civico della via della casa: ')
    prezzo: float = float(input('Inserisci il prezzo della casa: '))

    #vendità
    if (scelta == 0):
        piano: str = input('Inserisci il piano della casa: ')
        metri: int = int(input('Inserisci la metratura della casa: '))
        stanze: int = int(input('Inserisci il numero di stanza della casa: '))
        stato: str = 'LIBERO'

        print('Inserisci 0 se la casa non è affittata;')
        print('Inserisci 1 se la casa è affittata;')
        ris = input('--> ')

        if (ris == '1'):
            stato = 'OCCUPATO'

        jRequest = {"casa":{'catastale':catastale, 'indirizzo':indirizzo, 'civico':civico, 'piano': piano, 'metri': metri, 'stanze': stanze, 'prezzo': prezzo, 'stato': stato}
              
              , "operatore":{'user': user, 'password': password}}
    
    #affitto
    elif (scelta == 1):

        affitto: str = 'TOTALE'
        print('Inserisci 0 se l\'affitto è totale;')
        print('Inserisci 1 se l\'affitto è parziale;')
        ris = input('--> ')

        if (ris == '1'):
            affitto = 'PARZIALE'

        bagno: str = 'false'
        print('Inserisci 0 se il bagno non è personale;')
        print('Inserisci 1 se il bagno è personale;')
        ris = input('--> ')

        if (ris == '1'):
            bagno = 'true'

        jRequest = {"casa":{'catastale':catastale, 'indirizzo':indirizzo, 'civico':civico, 'affitto': affitto, 'bagno': bagno, 'prezzo': prezzo}
              
              , "operatore":{'user': user, 'password': password}}

    
    return jRequest

def EliminaCasa(user, password, scelta, fil = None):
    
    if (scelta == 1): catastale: str = input('Inserisci il codice castale della casa vhe vuoi eliminare: ')
    elif (scelta == 0): catastale: str = input('Inserisci il codice castale della casa che vuoi vendere: ')

    jRequest = {"casa":{'catastale': catastale}, "operatore":{'user': user, 'password': password, 'filiale': fil}}
    return jRequest

def CercaCasa(jsonDataRequest, scelta):
    
    if(scelta == 0): api_url = base_url + '/cerca_casa_vendita'
    elif(scelta == 1): api_url = base_url + '/cerca_casa_affitto'

    try:
        response = requests.post(api_url,json=jsonDataRequest,verify=False)
        print()
        print(response.status_code)
        print(response.headers["Content-Type"])
        data1 = response.json()
        #print(data1)

        case = data1['msg']
        if (type(case) == list):
            i = 0

            if(scelta == 0):
                for casa in case:
                    i += 1
                    print()
                    print()
                    print(f'Casa N.{i}')
                    print(f'Codice Catastale:   {casa[0]}')
                    print(f'Via:                {casa[1]}')
                    print(f'Civico:             {casa[2]}')
                    print(f'Piano:              {casa[3]}')
                    print(f'Metratura:          {casa[4]} mq')
                    print(f'Stanze:             {casa[5]}')
                    print(f'Prezzo:             {casa[6]} €')
                    print(f'Stato:              {casa[7]}')
                    print(f'Filiale Proponente: {casa[8]}')

            elif(scelta == 1):
                for casa in case:
                    i += 1
                    print()
                    print()
                    print(f'Casa N.{i}')
                    print(f'Codice Catastale:                 {casa[0]}')
                    print(f'Via:                              {casa[1]}')
                    print(f'Civico:                           {casa[2]}')
                    print(f'Tipo affitto:                     {casa[3]}')

                    if(casa[4]): casa[4] = 'si'
                    else: casa[4] = 'no'
                    print(f'Dis. bagno personale:             {casa[4]}')
                    print(f'Prezzo mensile:                   {casa[5]} €')
                    print(f'Filiale Proponente:               {casa[6]}')
        else: print(case)
    except:
        print('Problemi di connessione con il server, riprova più tardi')

def CreaInterfacciaRicerca(scelta):

    if (scelta == 0):
        
        print()
        print('1. Cerca casa in vendita per codice catastale')
        print('2. Cerca casa in vendita per indirizzo')
        print('3. Cerca casa in vendita per piano')
        print('4. Cerca casa in vendita per metratura')
        print('5. Cerca casa in vendita per numero di stanze')
        print('6. Cerca casa in vendita per prezzo')
        print('7. Cerca casa in vendita per stato')
        print('8. Cerca casa in vendita per filiale proponente')
        print('9. Exit')
    elif (scelta == 1):
        print()
        print('1. Cerca casa in affitto per codice catastale')
        print('2. Cerca casa in affitto per indirizzo')
        print('3. Cerca casa in affitto per tipo di affitto')
        print('4. Cerca casa in affitto con disponibilità di bagno personale')
        print('5. Cerca casa in affitto per prezzo mensile')
        print('6. Cerca casa in affitto per filiale proponente')
        print('7. Exit')
    else:
        print()
        print('. Exit')

def CreaInterfaccia(permesso):

    print()
    print('        Operazioni disponibili')

    if(permesso == 'w'):
        print()
        print('1. Inserisci casa in vendità')
        print('2. elimina casa in vendità')
        print('3. cerca casa in vendità')
        print('4. Inserisci casa in affitto')
        print('5. elimina casa in affitto')
        print('6. Cerca casa in affitto')
        print('7. Vendi casa')
        print('8. Exit')
    
    elif(permesso == 'r'):
        print()
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


login = True

while login:

    api_url = base_url + '/accedi'
    jsonDataRequest = accedi()

    try:

        response = requests.post(api_url,json=jsonDataRequest,verify=False)
        print()
        print(response.status_code)
        print(response.headers["Content-Type"])
        data1 = response.json()
        print(data1)
        msg = data1['msg']
    except:
        print('Problemi di connessione con il server, riprova più tardi')
        msg = 'ko'

    if msg == 'ok':

        login = False
        user: str = jsonDataRequest["operatore"]['user']
        password: str = data1['user'][1]
        permesso: str = data1['user'][2]
        fil_prop: str = data1['user'][3]

if not(login):
    CreaInterfaccia(permesso)
    print()
    sOper = input('Selezione operazione: ')

    #Controllo permessi
    if (permesso == 'w'):

        while (sOper != '8'):    

            #'1. Inserisci casa in vendità'
            if sOper == '1':
                
                if permesso == 'w':

                    api_url = base_url + '/add_casa_vendita'
                    jsonDataRequest = RichiediDatiCasa(user, password, 0)

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

            #'2. Elimina casa in vendità'
            elif sOper == '2':

                if permesso == 'w':
                    
                    api_url = base_url + '/elimina_casa_vendita'
                    jsonDataRequest = EliminaCasa(user, password, 1)

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

            #'3. Cerca casa in vendità'
            elif sOper == '3':  
                
                ris = 0
                
                while(ris != '9'):
                    
                    CreaInterfacciaRicerca(0)
                    ris = input('Selezione operazione: ')

                    #'Cerca casa in vendita per codice catastale'
                    if ris == '1':
                        
                        if permesso == 'w':

                            catastale = input('Inserisci il codice catastale della casa in vendità che stai cercando: ')
                            jsonDataRequest = {"casa":['catastale',catastale], "operatore":{'user': user, 'password': password}}

                            CercaCasa(jsonDataRequest, 0)

                        else: print('Permesso negato')

                    #'Cerca casa in vendita per indirizzo'
                    elif ris == '2':
                        
                        if permesso == 'w':

                            indirizzo = input('Inserisci il nome della via della casa in vendità che stai cercando: ')

                            if input('Vuoi aggiungere un numero civico(s/n): ') == 's':
                                
                                numero_civico = input('Inserisci il numero civico della casa in vendità che stai cercando: ')

                                jsonDataRequest = {"casa":['indirizzo', indirizzo, 'numero_civico', numero_civico], "operatore":{'user': user, 'password': password}}

                            else: jsonDataRequest = {"casa":['indirizzo', indirizzo], "operatore":{'user': user, 'password': password}}

                            CercaCasa(jsonDataRequest, 0)
                        
                        else: print('Permesso negato')

                    #'Cerca casa in vendita per piano'
                    elif ris == '3':
                        
                        if permesso == 'w':

                            piano = input('Inserisci il piano della casa in vendità che stai cercando: ')
                            jsonDataRequest = {"casa":['piano',piano], "operatore":{'user': user, 'password': password}}

                            CercaCasa(jsonDataRequest, 0)

                        else: print('Permesso negato')

                    #'Cerca casa in vendita per metratura'
                    elif ris == '4':

                        if permesso == 'w':


                            metri_max = input('Inserisci la metratura massima della casa in vendità che stai cercando: ')

                            try: metri_max = float(metri_max)
                            except:
                                ris = True
                            else: 
                                metri_max = int(metri_max)
                                ris = False 

                            while(ris):
                                print(f'Il valore {metri_max} non è valido.\n')
                                metri_max = input('Reinserisci la metratura massima della casa in vendità che stai cercando: ')
                                try: metri_max = float(metri_max)
                                except:
                                    ris = True
                                else: 
                                    metri_max = int(metri_max)
                                    ris = False

                            metri_min = input('Inserisci la metratura minima della casa in vendità che stai cercando: ')
                            
                            try: metri_min = float(metri_min)
                            except:
                                ris = True
                            else: 
                                metri_min = int(metri_min)
                                ris = False 

                            while(ris):
                                print(f'Il valore {metri_min} non è valido.\n')
                                metri_min = input('Reinserisci la metratura minima della casa in vendità che stai cercando: ')
                                
                                try: metri_min = float(metri_min)
                                except:
                                    ris = True
                                else: 
                                    metri_min = int(metri_min)
                                    ris = False 


                            jsonDataRequest = {"casa":['metri',metri_max,metri_min], "operatore":{'user': user, 'password': password}}

                            CercaCasa(jsonDataRequest, 0)

                        else: print('Permesso negato')


                    #'Cerca casa in vendita per numero di stanze'
                    elif ris == '5':
                        
                        if permesso == 'w':

                            vani = input('Inserisci il numero di stanze della casa in vendità che stai cercando: ')
                            ris = is_integer(vani)

                            while(ris):
                                print(f'Il valore {vani} non è valido.\n')
                                vani = input('Reinserisci il numero di stanze della casa in vendità che stai cercando: ')
                                ris = is_integer(vani)

                            vani = int(vani)

                            jsonDataRequest = {"casa":['vani',vani], "operatore":{'user': user, 'password': password}}

                            CercaCasa(jsonDataRequest, 0)

                        else: print('Permesso negato')

                    #'Cerca casa in vendita per prezzo'
                    elif ris == '6':
                        
                        if permesso == 'w':


                            prezzo_max = input('Inserisci il prezzo massimo del valore della casa in vendità che stai cercando(Max. 15 cifre): ')
                                
                            if ('.' in prezzo_max):

                                i = 16

                                x = prezzo_max.split(".")

                                x[1] = x[1][0] + x[1][1]

                                prezzo_max = x[0] + x[1]
                            else: i = 15

                            try: 
                                ris = False
                            except:
                                ris = True

                            while( (len(prezzo_max) > i)or(ris) ):

                                print(f'Il valore {prezzo_max} non è valido.\n')
                                prezzo_max = input('Reinserisci il prezzo massimo del valore della casa in vendità che stai cercando(Max. 15 cifre): ')

                                if ('.' in prezzo_max):

                                    i = 16

                                    x = prezzo_max.split(".")

                                    x[1] = x[1][0] + x[1][1]

                                    prezzo_max = x[0] + x[1]
                                else: i = 15

                                try: 
                                    ris = False
                                except:
                                    ris = True

                            prezzo_max = float(prezzo_max)

                            prezzo_min = input('Inserisci il prezzo minimo del valore della casa in vendità che stai cercando(Max. 15 cifre): ')
                            
                            if ('.' in prezzo_min):

                                i = 16

                                x = prezzo_min.split(".")

                                x[1] = x[1][0] + x[1][1]

                                prezzo_min = x[0] + x[1]
                            else: i = 15

                            try: 
                                
                                ris = False
                            except:
                                ris = True

                            while( (len(prezzo_min) > i)or(ris) ):

                                print(f'Il valore {prezzo_min} non è valido.\n')
                                prezzo_min = input('Reinserisci il prezzo minimo del valore della casa in vendità che stai cercando(Max. 15 cifre): ')
                                
                                if ('.' in prezzo_min):

                                    i = 16

                                    x = prezzo_min.split(".")

                                    x[1] = x[1][0] + x[1][1]

                                    prezzo_min = x[0] + x[1]
                                else: i = 15

                                try: 
                                    
                                    ris = False
                                except:
                                    ris = True

                            prezzo_min = float(prezzo_min)

                            jsonDataRequest = {"casa":['prezzo',prezzo_max,prezzo_min], "operatore":{'user': user, 'password': password}}

                            CercaCasa(jsonDataRequest, 0)

                        else: print('Permesso negato')

                    #'Cerca casa in vendita per stato'
                    elif ris == '7':
                        if permesso == 'w':

                            print('Inserisci 0 se stai cercando una casa non affittata(LIBERA)')
                            print('Inserisci 1 se stai cercando una casa affittata(OCCUPATA)')
                            ris = input('-->  ')

                            while ( (ris != '0')and(ris != '1') ):

                                print(f'Il valore {ris} non è valido.\n')
                                print('Inserisci 0 se stai cercando una casa non affittata(LIBERA)')
                                print('Inserisci 1 se stai cercando una casa affittata(OCCUPATA)')
                                ris = input('-->  ')

                            if ris == '0':
                                stato = 'LIBERO'
                            elif ris == '1':
                                stato = 'OCCUPATO'
                            else: stato = None

                            jsonDataRequest = {"casa":['stato',stato], "operatore":{'user': user, 'password': password}}

                            CercaCasa(jsonDataRequest, 0)

                        else: print('Permesso negato')

                    #'Cerca casa in vendita per filiale proponente'
                    elif ris == '8':
                        
                        if permesso == 'w':

                            filiale_proponente = input('Inserisci il codice della filiale che sta proponendo la casa in vendità che stai cercando: ')
                            jsonDataRequest = {"casa":['filiale_proponente',filiale_proponente], "operatore":{'user': user, 'password': password}}

                            CercaCasa(jsonDataRequest, 0)

                        else: print('Permesso negato')
                        
            #'4. Inserisci casa in affitto'
            elif sOper == '4':

                if(permesso == 'r')or(permesso == 'w'):

                    api_url = base_url + '/add_casa_affitto'
                    jsonDataRequest = RichiediDatiCasa(user, password, 1)

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

            #'5. Elimina casa in affitto'
            elif sOper == '5':

                if permesso == 'w':
                    
                    api_url = base_url + '/elimina_casa_affitto'
                    jsonDataRequest = EliminaCasa(user, password, 1)

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

            #'6. Cerca casa in affitto'
            elif sOper == '6':  
                
                ris = 0
                
                while(ris != '7'):
                    
                    CreaInterfacciaRicerca(1)
                    ris = input('Selezione operazione: ')

                    #'Cerca casa in affitto per codice catastale'
                    if ris == '1':
                        
                        if permesso == 'w':

                            catastale = input('Inserisci il codice catastale della casa in affitto che stai cercando: ')
                            jsonDataRequest = {"casa":['catastale',catastale], "operatore":{'user': user, 'password': password}}

                            CercaCasa(jsonDataRequest, 1)

                        else: print('Permesso negato')

                    #'Cerca casa in affitto per indirizzo'
                    elif ris == '2':
                        
                        if permesso == 'w':

                            indirizzo = input('Inserisci il nome della via della casa in affitto che stai cercando: ')

                            if input('Vuoi aggiungere un numero civico(s/n): ') == 's':
                                
                                civico = input('Inserisci il numero civico della casa in affitto che stai cercando: ')

                                jsonDataRequest = {"casa":['indirizzo', indirizzo, 'civico', civico], "operatore":{'user': user, 'password': password}}

                            else: jsonDataRequest = {"casa":['indirizzo', indirizzo], "operatore":{'user': user, 'password': password}}

                            CercaCasa(jsonDataRequest, 1)
                        
                        else: print('Permesso negato')

                    #'Cerca casa in affitto per tipo di affitto'
                    elif ris == '3':
                        if permesso == 'w':

                            print('Inserisci 0 se stai cercando una casa con affitto TOTALE')
                            print('Inserisci 1 se stai cercando una con affitto PARZIALE')
                            ris = input('-->  ')

                            while ( (ris != '0')and(ris != '1') ):

                                print(f'Il valore {ris} non è valido.\n')
                                print('Inserisci 0 se stai cercando una casa con affitto TOTALE')
                                print('Inserisci 1 se stai cercando una con affitto PARZIALE')
                                ris = input('-->  ')

                            if ris == '0':
                                tipo_affitto = 'TOTALE'
                            elif ris == '1':
                                tipo_affitto = 'PARZIALE'
                            else: stato = None

                            jsonDataRequest = {"casa":['tipo_affitto',tipo_affitto], "operatore":{'user': user, 'password': password}}

                            CercaCasa(jsonDataRequest, 1)

                        else: print('Permesso negato')

                    #'Cerca casa in affitto con bagno privato'
                    elif ris == '4':
                        if permesso == 'w':

                            print('Inserisci 0 se stai cercando una casa in affitto con bagno privato')
                            print('Inserisci 1 se stai cercando una casa in affitto senza un bagno privato')
                            ris = input('-->  ')

                            while ( (ris != '0')and(ris != '1') ):

                                print(f'Il valore {ris} non è valido.\n')
                                print('Inserisci 0 se stai cercando una casa in affitto con bagno privato')
                                print('Inserisci 1 se stai cercando una casa in affitto senza un bagno privato')
                                ris = input('-->  ')

                            if ris == '0':
                                bagno_personale = 'true'
                            elif ris == '1':
                                bagno_personale = 'false'
                            else: stato = None

                            jsonDataRequest = {"casa":['bagno_personale',bagno_personale], "operatore":{'user': user, 'password': password}}

                            CercaCasa(jsonDataRequest, 1)

                        else: print('Permesso negato')

                    #'Cerca casa in affitto per prezzo'
                    elif ris == '5':
                                            
                        if permesso == 'w':


                            prezzo_max = input('Inserisci il prezzo massimo del valore della casa in affitto che stai cercando(Max. 15 cifre): ')
                                
                            if ('.' in prezzo_max):

                                i = 16

                                x = prezzo_max.split(".")

                                x[1] = x[1][0] + x[1][1]

                                prezzo_max = x[0] + x[1]
                            else: i = 15

                            try: 
                                ris = False
                            except:
                                ris = True

                            while( (len(prezzo_max) > i)or(ris) ):

                                print(f'Il valore {prezzo_max} non è valido.\n')
                                prezzo_max = input('Reinserisci il prezzo massimo del valore della casa in affitto che stai cercando(Max. 15 cifre): ')

                                if ('.' in prezzo_max):

                                    i = 16

                                    x = prezzo_max.split(".")

                                    x[1] = x[1][0] + x[1][1]

                                    prezzo_max = x[0] + x[1]
                                else: i = 15

                                try: 
                                    ris = False
                                except:
                                    ris = True

                            prezzo_max = float(prezzo_max)

                            prezzo_min = input('Inserisci il prezzo minimo del valore della casa in affitto che stai cercando(Max. 15 cifre): ')
                            
                            if ('.' in prezzo_min):

                                i = 16

                                x = prezzo_min.split(".")

                                x[1] = x[1][0] + x[1][1]

                                prezzo_min = x[0] + x[1]
                            else: i = 15

                            try: 
                                
                                ris = False
                            except:
                                ris = True

                            while( (len(prezzo_min) > i)or(ris) ):

                                print(f'Il valore {prezzo_min} non è valido.\n')
                                prezzo_min = input('Reinserisci il prezzo minimo del valore della casa in affitto che stai cercando(Max. 15 cifre): ')
                                
                                if ('.' in prezzo_min):

                                    i = 16

                                    x = prezzo_min.split(".")

                                    x[1] = x[1][0] + x[1][1]

                                    prezzo_min = x[0] + x[1]
                                else: i = 15

                                try: 
                                    
                                    ris = False
                                except:
                                    ris = True

                            prezzo_min = float(prezzo_min)

                            jsonDataRequest = {"casa":['prezzo_mensile',prezzo_max,prezzo_min], "operatore":{'user': user, 'password': password}}

                            CercaCasa(jsonDataRequest, 1)

                        else: print('Permesso negato')

                    #'Cerca casa in affitto per filiale proponente'
                    elif ris == '6':
                        
                        if permesso == 'w':

                            filiale_proponente = input('Inserisci il codice della filiale che sta proponendo la casa in affitto che stai cercando: ')
                            jsonDataRequest = {"casa":['filiale_proponente',filiale_proponente], "operatore":{'user': user, 'password': password}}

                            CercaCasa(jsonDataRequest, 1)

                        else: print('Permesso negato')

            #'7. Vendi casa'
            elif sOper == '7':
                
                if permesso == 'w':
                    
                    api_url = base_url + '/vendi_casa'
                    jsonDataRequest = EliminaCasa(user, password, 0, fil_prop)

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

        else:
            print('Arrivederci')

    elif (permesso == 'r'):
        pass

        CreaInterfaccia(permesso)
        print()
        sOper = input('Selezione operazione: ')
    else :
        print('Permesso Negato')