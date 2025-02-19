from flask import Flask, render_template, request

api = Flask(__name__)

utenti: list[list[str]] = [['Mario','Aa@12345','1','Roma','0'],['Luigi','Bb$23456','1','Pescara','0'],['Francesca','Cc!34567','2','Milano','0']]

@api.route('/', methods=['GET'])
def index():
    
    return render_template('index.html')


@api.route('/regok', methods=['GET'])
def reg_ok():
    
    return render_template('reg_ok.html')

@api.route('/regko', methods=['GET'])
def reg_ko():
    
    return render_template('reg_ko.html')

@api.route('/registrati', methods=['GET'])
def registra():
    utente: list[str] = [str(request.args.get("fname")),str(request.args.get("fpassword")), str(request.args.get("fsesso")), str(request.args.get("fComune")),'0']
    #print(utente)

    #Devo prendere tutti i dati e verificare se la terna c'è nel vettore degli utenti

    if(utente in utenti):
        ind: int = utenti.index(utente)
        #print(utenti[ind])
        utenti[ind][4] = '1'
        #print(utenti[ind])
        return reg_ok()#render_template('reg_ok.html')
    else:
        return reg_ko()#render_template('reg_ko.html')
    
@api.route('/login', methods=['GET'])
def login():
    
    return render_template('login.html')

@api.route('/PersonalPage', methods=['GET'])
def peronal_page():
    
    nome: str = str(request.args.get("fname"))
    sesso: str = str(request.args.get("fsesso"))
    if sesso == '1':
        sesso = 'un Maschio nato a'
    elif sesso == '2':
        sesso = 'una Femmina nata a'

    comune: str = str(request.args.get("fComune"))

    response = f'''<html>
    <head>
        <title>Personal Page</title>
    </head>
    <body>
        <h1>Ciao {nome}, sei {sesso} {comune}</h1>
    </body>
</html>'''

    return response

@api.route('/accedi', methods=['GET'])
def accedi():
    utente: list[str] = [str(request.args.get("fname")),str(request.args.get("fpassword")), str(request.args.get("fsesso")), str(request.args.get("fComune")),'1']
    
    if(utente in utenti):

        return peronal_page()#render_template('reg_ok.html')
    else:
        return reg_ko()#render_template('reg_ko.html')

api.run(host='0.0.0.0',port=8085)