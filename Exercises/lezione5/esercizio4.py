def frequency_dict(elements: list) -> dict:
    
    dizio: dict = {}

    for key in elements:
        
        if key in dizio:

            dizio[key] += 1

        elif key not in dizio:

            dizio.update({key: 1})

    return dizio



print(frequency_dict(['mela', 'banana', 'mela']))