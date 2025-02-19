from flask import Flask, render_template, request

api = Flask(__name__)

users: list[list[str]] = [['Mario','Aa@12345','0'],['Luigi','Bb$23456','0'],['Francesca','Cc!34567','0'],['a','Aa@12345','0']]

@api.route('/', methods=['GET'])
def index():
    
    return render_template('homepage.html')

@api.route('/registrazione', methods=['GET'])
def registrazione():
    
    return render_template('registrazione.html')

@api.route('/login', methods=['GET'])
def login():
    
    return render_template('login.html')

@api.route('/registrati', methods=['GET'])
def registra():
    utente: list[str] = [str(request.args.get("fname")),str(request.args.get("fpassword")),'0']
    
    if(utente in users):

        ind: int = users.index(utente)
        users[ind][2] = '1'
        return login()
    else:
        return registrazione()

@api.route('/accedi', methods=['GET'])
def accedi():

    #return personal_page(['Mario','Aa@12345','1','Roma','0'])

    utente: list[str] = [str(request.args.get("fname")),str(request.args.get("fpassword")),'1']
    
    for user in users:

        if (user[0] == utente[0])and(user[1]==utente[1])and(user[2] == '1'):
            return personal_page(user)
    
    return index()

@api.route('/PersonalPage', methods=['GET'])
def personal_page(utente):
    
    nome: str = utente[0]
    
    response = f'''
    <html>
        <head>
            <title>Personal Page</title>
        </head>
        <body>
            <h1>{nome.capitalize()}</h1>
        </body>
    </html>
    '''

    return response

api.run(host='0.0.0.0',port=8085)