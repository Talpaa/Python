class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        
        return  f'{self.val}{self.next}'
        
def reverse_list(head: ListNode) -> list[int]:
    
    stringa: str = str(head)

    stringa = stringa.replace('None', "")

    lista: list = []

    for i in stringa:

        lista.insert(0, int(i))

    return lista


head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
print(reverse_list(head))#Output [5, 4, 3, 2, 1]

head = ListNode(val=1, next=ListNode(val=2))
print(reverse_list(head))#Output [2, 1]

	

