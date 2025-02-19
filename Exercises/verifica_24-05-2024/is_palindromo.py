class Node:

    def __init__(self, node) -> None:
        
        self.node = node
        self.next = None

class LinkedList:
    
    def __init__(self) -> None:
       
       self.head: list = []

    def append(self, x: int):

        node: Node = Node(x)

        self.head.append(node)

        if node.next == None:

            i = self.head.index(node)

            if i-1 >= 0:
                self.head[i-1].next = node
        


        
def is_palindrome(head: Node) -> list[int]:
    
    lista: list = []

    for i in head:

        lista.append(i.node)

    lista_reversed: list = reversed(lista)

    lista.reverse()
    lista_revers: list = lista.copy()
    lista.reverse()

    if lista == lista_revers:

        return True
    
    else:

        return False



ll1 = LinkedList()
for value in [1, 2, 3, 2, 1]:
    ll1.append(value)


print(is_palindrome(ll1.head))