def print_seq():

    message: str = 'Sequenza a):\n'
    for num in range(1,8):

        message += f'{num}\n'

    print(message)

    message = 'Sequenza b):\n'
    num: int = 3
    for _ in range(5):

        message += f'{num}\n'
        
        num += 5

    print(message)

    message = 'Sequenza c):\n'
    num= 20
    for _ in range(6):

        message += f'{num}\n'

        num -= 6

    print(message)

    message = 'Sequenza d):\n'
    num= 19
    for _ in range(5):

        message += f'{num}\n'

        num += 8

    print(message)


print_seq()
'''
Sequenza a):
1
2
3
4
5
6
7

Sequenza b):
3
8
13
18
23

Sequenza c):
20
14
8
2
-4
-10

Sequenza d):
19
27
35
43
51
'''