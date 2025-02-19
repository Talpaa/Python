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

    def get_node(self):
        pass
        
def has_cycle(head: Node) -> list[int]:
    pass



 	

ll1 = LinkedList()
for i in range(5):
    ll1.append(i)
node1 = ll1.get_node(1)  # Node with value 1
node4 = ll1.get_node(4)  # Node with value 4
node4.next = node1  # Creating a cycle

print(has_cycle(ll1.head))  #Output True