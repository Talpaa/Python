def trova_chiave_per_valore(dizio: dict[str: int], num: int)->str|None:

    for key in dizio:

        if dizio[key] == num:

            return key
        
    return None

print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))#b

print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3'))#None