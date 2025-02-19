#controlla per ogni lista che gli viene inviata che non ci siano doppioni
def find_duplicates(linea: list):
            
    cifre: list = ['1','2','3','4','5','6','7','8','9']

    for i in linea:

        if (i in cifre):

            cifre.remove(i)

        elif(not(i == '.')): 

            return False
        
    return True


def valid_sudoku(board: list[list[str]]) -> bool:
    # la tavola del sudo viene rapperentata come una matrice (lista di liste)
    # con 9 righe e 9 colonne
    
    valid: bool = True

    #invia alla funzione find_duplicates ogni linea del sudoku per cercare doppioni
    for lin in board:

        valid = find_duplicates(lin)

        if not(valid):

            return valid
        
    #permette di creare una lista per ogni colonna del sudoku, per poi inviarla a find_duplicates
    for lin in range(9):

        colonna: list = []

        for col in board:

            colonna.append(col[lin])

        valid = find_duplicates(colonna)

        if not(valid):

            return valid

    #permette di creare una lista per ogni riquadro del sudoku, per poi inviarla a find_duplicates
    box: list = []
    for i in board:

        for n in range(3):

            box.append(i[n])

        ind: int = (board.index(i))+1
        if (ind % 3) == 0:

            valid = find_duplicates(box)

            if not(valid):

                return valid
            
            box = []

    box: list = []
    for i in board:

        for n in range(3,6):

            box.append(i[n])

        ind: int = (board.index(i))+1
        if (ind % 3) == 0:

            valid = find_duplicates(box)

            if not(valid):

                return valid
            
            box = []

    box: list = []
    for i in board:

        for n in range(6,9):

            box.append(i[n])

        ind: int = (board.index(i))+1
        if (ind % 3) == 0:

            valid = find_duplicates(box)

            if not(valid):

                return valid
            
            box = []

    return valid


board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku(board))#Output True

board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku(board))#Output False