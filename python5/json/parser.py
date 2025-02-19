import json

def SerializaJson(dData,file_path)->True|False:
    
    try:
        with open(file=file_path, mode='w') as file:

            file.write(json.dumps(dData))
    except:
        return False
    else:
        return True

def DeserializeJson(file_path)-> dict:
    
    with open(file=file_path, mode='r') as file:

        return json.loads(file.read())


file_path: str = './dizionari_json/mydict_1.json'

mydict_1 = { "brand": "Ford",
"electric": False,
"year": 1964,
"colors": ["red", "white", "blue"]}

print(SerializaJson(mydict_1, file_path))

dict1 = DeserializeJson(file_path)
print(dict1)