def merge_dictionaries(dizio1: dict[str: int], dizio2: dict[str: int])->dict[str: int]:

    for key in dizio2:

        if key in dizio1:
            dizio1[key] += dizio2[key]

        else:

            dizio1[key] = dizio2[key]

    return dizio1

print(merge_dictionaries({'x': 5}, {'x': -5}))#{'x': 0}