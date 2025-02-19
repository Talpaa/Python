def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    
    contact: dict = {'profile': name, 'email': email, 'telefono': telefono}

    return contact

def update_contact(dictionary: dict, name: str, email: str =1, telefono: int=1) -> dict:
    
    if email == 1:
        
        dictionary['telefono'] = telefono

        return dictionary

    elif telefono == 1:
        
        dictionary['email'] = email

        return dictionary
    
    else:

        dictionary['telefono'] = telefono
        dictionary['email'] = email

        return dictionary




#contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
#print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))    #output {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 788787}
#print(update_contact(contact, "Mario Rossi", telefono=123456789))   #output {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 123456789}



contact = create_contact("Laura Neri", email="laura.neri@domain.com")   
print(create_contact("Laura Neri", email="laura.neri@domain.com"))  #output {'profile': 'Laura Neri', 'email': 'laura.neri@domain.com', 'telefono': None}
print(update_contact(contact, "Laura Neri", email="laura.new@domain.com", telefono=84736736))   #output {'profile': 'Laura Neri', 'email': 'laura.new@domain.com', 'telefono': 84736736}

	
