def Serializza(lista: list)->str:
    
    return str(lista)

def Deserializza(stringa: str)->list:
    
    lista: list[str] = []
    list_chr: list = list(stringa)

    if ('[' in list_chr)and(']' in list_chr):

        list_chr.remove('[')
        list_chr.remove(']')

    ap: bool = False

    for char in list_chr:

        if(ap)and(not(char == "'")):

            lista_prov.append(char)

        if (char == "'")and(not(ap)):

            ap = True
            lista_prov: list[str] = []

        elif (char == "'")and(ap):

            nome: str = ''
            for let in lista_prov:

                nome += let

            lista.append(nome)
            ap = False

    return lista

lista: list[str] = ['mario', 'gino', 'lucrezia']

lista_serializzata: str = Serializza(lista)

lista_deserializzata: list[str] = Deserializza(lista_serializzata)

print(lista_serializzata)
print(type(lista_serializzata))

print(lista_deserializzata)
print(type(lista_deserializzata))