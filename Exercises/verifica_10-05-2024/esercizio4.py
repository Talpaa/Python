def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    
    dizionario: dict = {}
    for i in voti:
            
            if i['nome'] not in dizionario:

                dizionario[i['nome']] = [i['voto']]

            else:

                dizionario[i['nome']].append(i['voto']) 

    return dizionario


print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}])) #output {'Alice': [90, 85], 'Bob': [75]}

print(aggrega_voti([])) #output{}