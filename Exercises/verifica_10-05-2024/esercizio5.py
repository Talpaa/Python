def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    
    dizionario: dict = {}

    for key in prodotti:

        if prodotti[key] > 20:

            prodotto_scontato: float = (prodotti[key] - (prodotti[key]/100)*10)
            dizionario[key] = prodotto_scontato

    return dizionario

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0})) #output {'Zaino': 45.0, 'Quaderno': 19.8}

print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) #output {}