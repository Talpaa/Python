def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    

    for key in dict2:

        if key in dict1:

            dict1[key] = dict1[key] + dict2[key]

        else:

            dict1.update({key: dict2[key]})


    return dict1



print(merge_dictionaries({'x': 5}, {'x': -5}))