def check_access(user: str, password: str, controllo: bool):

    if (user == 'admin')and(password == '12345')and(controllo):

        return f'Accesso consentito'
    
    else:

        return f'Accesso negato'

print(check_access("admin", "12345", True))#Accesso consentito

print(check_access("admin", "54321", True))#Accesso negato