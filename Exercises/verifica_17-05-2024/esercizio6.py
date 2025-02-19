'''class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        
        message: str =  f'{self.val}\n'\
              +f'{self.left}    {self.right}'
        
        return message
        
def symmetric(tree: list[int]) -> bool:
    
    indice: int = len(tree)
    albero: list[TreeNode] = []
    for i in range(0, indice):
        

        if ((2*i + 1) < (indice))and((2*(i+1)) < (indice)):

            albero.append(TreeNode(val=i,left=tree[(2*i + 1)],right=tree[(2*(i+1))]))

        elif((2*i + 1) < (indice)):

            albero.append(TreeNode(val=i,left=tree[(2*i + 1)]))

        elif((2*(i+1)) < (indice)):

            albero.append(TreeNode(val=i,right=tree[(2*(i+1))]))

        else:
            albero.append(TreeNode(val = i))'''


def symmetric(tree: list[int])->bool:

    def check_symmetry(indice_sinistro, indice_destro):

        if (indice_sinistro >= len(tree) )and(indice_destro) >= len(tree):

            return True
        
        if (indice_sinistro >= len(tree))or(indice_destro >= len(tree)):

            return False
        
        if tree[indice_sinistro] != tree[indice_destro]:
            return False
        
        return check_symmetry(2*indice_sinistro + 1,2 * indice_destro + 2) and check_symmetry(2 * indice_sinistro + 2,2 * indice_destro + 1)

    #se la lista è vuota l'albero è sicuramente simmetrico quindi restituisco True
    if not tree:
        return True

    return check_symmetry(1,2)






        


 	

print(symmetric([1,2,2,3,4,4,3]))#Output True

print(symmetric([1,2,2,None,3,None,3]))#Output False

print(symmetric([1,2,2,None,3,3,None]))#Output True

print(symmetric([1,2,2,3,None,None,3]))#Output True