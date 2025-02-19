def ciao(name: str)-> str:

    return f'Ciao, {name}'

def salve(name: str)->str:

    return f'Salve, {name}'

def saluta_bob(func)->str:

    return func('Bob')

print(saluta_bob(ciao))
print(saluta_bob(salve))

def parent():

    print('Sono in parent')

    def first_child():

        print('Sono in first child')

    return first_child()

def decorator(func):

    def wrapper():

        import time

        start = time.time()

        func()

        print(f'Time elapsed: {time.time() - start}')

    return wrapper

def ciao():

    print(f'Ciao!')

ciao = decorator(ciao)

ciao()

parent()