def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    
    for key in dizionario:

        if dizionario[key] == valore:

            return key


print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200)) #output b

print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3')) # output None