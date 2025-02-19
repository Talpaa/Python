def verifica_condizioni(x: bool, y: bool, z: bool)->str:

    message: str = 'Azione '

    if (x and (y or z)):

        message += 'permessa'

    else:

        message += 'negata'

    return message

        

print(verifica_condizioni(True, False, True))#Azione permessa

print(verifica_condizioni(True, False, False))#Azione negata