import json, requests
from flask import Flask, render_template, request

api = Flask(__name__)

base_url = 'https://127.0.0.1:8080'

global utente

@api.route('/', methods=['GET'])
def index():
    return render_template('homepage.html')

@api.route('/registrazione', methods=['GET'])
def registrazione():
    return render_template('registrazione.html')

@api.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@api.route('/creacittadino', methods=['GET'])
def crea_cittadino():
    return render_template('crea_cittadino.html')

@api.route('/modificacittadino', methods=['GET'])
def modifica_cittadino():
    return render_template('modifica_cittadino.html')

@api.route('/eliminacittadino', methods=['GET'])
def elimina_cittadino():
    return render_template('elimina_cittadino.html')

@api.route('/visualizzacittadino', methods=['GET'])
def visualizza_cittadino():
    return render_template('visualizza_cittadino.html')
    
@api.route('/registrati', methods=['GET'])
def registra():
    data1 = {}

    name = str(request.args.get("fname"))
    password = str(request.args.get("fpassword"))

    api_url = base_url + '/registra'
    jsonDataRequest = {"operatore":{'user': name, 'password': password}}

    try:

        response = requests.post(api_url,json=jsonDataRequest,verify=False)
        print()
        print(response.status_code)
        print(response.headers["Content-Type"])
        data1 = response.json()
        print(data1)
    except:
        print('Problemi di connessione con il server, riprova più tardi')
        data1 = {'msg': ''}

    if (data1['msg'] == 'ok')or(data1['msg'] == 'Utente già Registrato'):

        return login()
    return registrazione()

@api.route('/accedi', methods=['GET'])
def accedi():
    global utente
    name = str(request.args.get("fname"))
    password = str(request.args.get("fpassword"))

    api_url = base_url + '/accedi'
    jsonDataRequest = {"operatore":{'user': name, 'password': password}}

    try:

        response = requests.post(api_url,json=jsonDataRequest,verify=False)
        print()
        print(response.status_code)
        print(response.headers["Content-Type"])
        data1 = response.json()
        print(data1)
        utente = data1['user']
    except:
        print('Problemi di connessione con il server, riprova più tardi')

    if (data1['msg'] == 'ok'):

        return personal_page(utente, 0)
    elif (data1['msg'] == 'not ok'):
        return registrazione()
    return login()

@api.route('/PersonalPage', methods=['GET'])
def personal_page(utente, i):

    response = ''
    
    if (i == 0):
        response = f'''
        <html>
            <head>
                <title>Personal Page</title>
            </head>	
            
            <body>

        '''

    if utente[2] == 'w':
        
        response += f'''
                <h1 align="left">Operatore {utente[0].title()} | Operazioni:</h1>
                <br><br>
                    <table align="center"><tr>
                                <h1><td>&emsp;&emsp;&emsp;&emsp;
                                    <td>
                                        <form action="/creacittadino" method="get">
                                            <input type="submit" value="|    Inserisci cittadino (es. atto di nascita)">
                                        </form>
                                </h1></td>
                            <tr>
                                <h1><td>&emsp;&emsp;&emsp;&emsp;
                                    <td>
                                        <form action="/modificacittadino" method="get">
                                            <input type="submit" value="|    Modifica dati cittadino (es. cert. residenza)">
                                        </form>
                                </h1></td>
                            <tr>
                                <h1><td>&emsp;&emsp;&emsp;&emsp;
                                    <td>
                                        <form action="/eliminacittadino" method="get">
                                            <input type="submit" value="|    Elimina cittadino">
                                        </form>
                                </h1></td>
                            <tr>
                                <h1><td>&emsp;&emsp;&emsp;&emsp;
                                    <td>
                                        <form action="/visualizzacittadino" method="get">
                                            <input type="submit" value="|    Richiedi dati cittadino (es. cert. residenza)">
                                        </form>
                                </h1></td>
                        </tr>
                </table>

    '''
    elif utente[2] == 'r':
        
        response += f'''
                <br><br>
                <a href="./templates/visualizza_cittadino.html"><h1>|    Richiedi dati cittadino (es. cert. residenza)</h1></a>.
            
    '''
    else:
        return index()
    
    if (i==0):
        response += f'''
                </body>
        </html>
    '''

    return response

@api.route('/visualizza', methods=['GET'])
def visualizza():
    data1 = {}

    global utente
    cf = str(request.args.get("fcf"))
    api_url = base_url + '/info_cittadino'
    jsonDataRequest = {'user': cf}

    try:

        response = requests.post(api_url,json=jsonDataRequest,verify=False)
        print()
        print(response.status_code)
        print(response.headers["Content-Type"])
        data1 = response.json()
        print(data1)
    except:
        print('Problemi di connessione con il server, riprova più tardi')
        data1 = {'msg': ''}

    if (data1['msg'] == 'ok'):

        return visual_page(data1['info'], 0)
    
    return personal_page(utente, 0)

@api.route('/aggiungi', methods=['GET'])
def aggiungi():
    data1 = {}

    name = str(request.args.get("fname"))
    surname = str(request.args.get("fsurname"))
    data = str(request.args.get("fdate"))
    cf = str(request.args.get("fcf"))
 
    api_url = base_url + '/add_cittadino'
    jsonDataRequest = {"cittadino":{'nome':name, 'cognome':surname, 'dataNascita':data,'codiceFiscale': cf}}

    try:

        response = requests.post(api_url,json=jsonDataRequest,verify=False)
        print()
        print(response.status_code)
        print(response.headers["Content-Type"])
        data1 = response.json()
    except:
        print('Problemi di connessione con il server, riprova più tardi')
        data1 = {'msg': ''}

    if (data1['msg'] == 'ok'):

        return visual_page(data1['info'], 1)
    
    return personal_page(utente, 0)

@api.route('/rimuovi', methods=['GET'])
def rimuovi():
    data1 = {}

    cf = str(request.args.get("fcf"))
 
    api_url = base_url + '/elimina_cittadino'
    jsonDataRequest = {"cittadino":{'codiceFiscale': cf}}

    try:

        response = requests.post(api_url,json=jsonDataRequest,verify=False)
        print()
        print(response.status_code)
        print(response.headers["Content-Type"])
        data1 = response.json()
    except:
        print('Problemi di connessione con il server, riprova più tardi')
        data1 = {'msg': ''}

    print(data1)
    if (data1['msg'] == 'Cittadino eliminato'):

        return visual_page(data1['info'], 3)
    
    return personal_page(utente, 0)

@api.route('/modifica', methods=['GET'])
def modifica():
    data1 = {}

    cf = str(request.args.get("fcf"))
    name = str(request.args.get("fname"))
    surname = str(request.args.get("fsurname"))
    data = str(request.args.get("fdate"))
    ncf = str(request.args.get("fncf"))

    api_url = base_url + '/modifica_cittadino'
    jsonDataRequest = {"cittadino":{'codiceFiscale': cf}, "modifiche": {'codiceFiscale': ncf, 'nome':name, 'cognome':surname, 'dataNascita':data}}

    try:

        response = requests.post(api_url,json=jsonDataRequest,verify=False)
        print()
        print(response.status_code)
        print(response.headers["Content-Type"])
        data1 = response.json()
    except:
        print('Problemi di connessione con il server, riprova più tardi')
        data1 = {'msg': ''}

    print(data1)
    if (data1['msg'] == 'modifiche effettuate'):

        return visual_page(data1['info'], 4)
    
    return personal_page(utente, 0)

@api.route('/VisualPage', methods=['GET'])
def visual_page(cittadino, i):
    global utente

    if (i==0):
        response = f'''
        <html>
            <head>
                <title>Visual Page</title>
            </head>	
            
            <body>
                <h1 align="center">Dati del cittadino:</h1>
        '''
    elif (i==1):
        response = f'''
        <html>
            <head>
                <title>Visual Page</title>
            </head>	
            
            <body>
                <h1 align="center">Dati del cittadino appena creato:</h1>
        '''
    elif (i==3):

        response = f'''
        <html>
            <head>
                <title>Visual Page</title>
            </head>	
            
            <body>
                <h1 align="center">Dati del cittadino appena eliminato:</h1>
        '''
    elif (i==4):

        response = f'''
        <html>
            <head>
                <title>Visual Page</title>
            </head>	
            
            <body>
                <h1 align="center">I nuovi dati del cittadino appena modificato:</h1>
        '''

    response += f'''
    
            <br><br>
            <table align="center"><tr>
                        <h1><td>&emsp;&emsp;&emsp;&emsp;
                            <td>
                                Codice Fiscale: {cittadino[0]}
                        </h1></td>
                    <tr>
                        <h1><td>&emsp;&emsp;&emsp;&emsp;
                            <td>
                                Nome: {cittadino[1]}
                        </h1></td>
                    <tr>
                        <h1><td>&emsp;&emsp;&emsp;&emsp;
                            <td>
                                Cognome: {cittadino[2]}
                        </h1></td>
                    <tr>
                        <h1><td>&emsp;&emsp;&emsp;&emsp;
                            <td>
                                Data di Nascita: {cittadino[3]}
                        </h1></td>
                    <tr>
                        <h1><td>&emsp;&emsp;&emsp;&emsp;
                            <td>
                                &emsp;&emsp;&emsp;&emsp;
                        </h1></td>
                        <tr>
                        <h1><td>&emsp;&emsp;&emsp;&emsp;
                            <td>
                                {personal_page(utente, 1)}
                        </h1></td>
                </tr>
            </table>
        </body>
    </html>
    '''

    return response

api.run(host='0.0.0.0',port=8085)

