def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:

    dizio: dict[str:float] = {}
    
    for key in prodotti:

        prodotto: float = prodotti[key] + (prodotti[key]/100)*10

        if prodotti[key] < 50.0:

            dizio[key] = round(prodotto, 2)

    return dizio



print(filtra_e_mappa({"prodotto1": 30.0, "prodotto2": 60.0, "prodotto3": 45.0}))