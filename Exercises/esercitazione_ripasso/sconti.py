def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:

    prodotti_scontati: dict[str: float] = {}
    
    for key in prodotti:

        prodotto = prodotti[key]

        if prodotto > 20.0:

            prodotti_scontati[key] = prodotto - (prodotto * 0.1)

    return prodotti_scontati

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))#{'Zaino': 45.0, 'Quaderno': 19.8}
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0}))#{}