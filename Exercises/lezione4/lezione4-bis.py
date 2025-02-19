
#esercizio 1

def palindromi(x: str)->bool:

    str_reverse = x[::-1]    

    if x == str_reverse:

        print(f"\n\nIl numero {x} è palindromo")

    else:
        print(f"\n\nIl numero {x} non è palindromo")

    return x == str_reverse



x: int = 7665885667
str_x = str(x)

y: int = 1234567890
str_y = str(y)

palindromi(str_x)

palindromi(str_y)

#esercizio 2

def ultima_parola(s: str)->int:

    a: int = 0
    b: int = 0

    for i in s[::-1]:

        if i != " ":

            a += 1

        elif(i == " ")and(a != 0):

            return a


s1: str = "Hello world     "

ultima = ultima_parola(s1)
print(f"\n\nL'ultima parola della frase è lunga {ultima}")

s2: str = "fly me to the moon"
ultima = ultima_parola(s2)
print(f"\nL'ultima parola della frase è lunga {ultima}")

s3: str = "lufy is still joyboy"
ultima = ultima_parola(s3)
print(f"\nL'ultima parola della frase è lunga {ultima}")



#esercizio 3

def convert_to_title(col_number: int)->str:

    result: str = ""
    alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    while col_number > 26:

        a = (col_number-1) % 26
        col_number = (col_number // 26)-1

        result = alfabeto[a]+result


    result = alfabeto[col_number]+result

    return result 

titolo: int = 1214
coversione: str = convert_to_title(titolo)

print(coversione)


#esercizio 4


def maggiore_di_element(ls: list)->int:

    for i in set(ls):

        if ls.count(i) > (len(ls)/2):

            return i

    return None

ls = [3,3,3,3,3,3,3,2,2,2,2,2,2,2]

num: int = maggiore_di_element(ls)


if num != None:

    print(f"Il numero {num} è presente in più del 50% delle poszioni della lista")

else:

    print(f"Nessun numero della lista è presente in più del 50% delle poszioni della lista")




#esercizio 5

def move_zeroes(nums: list[int]):

    z: int = 0
    ls = []

    for i in nums:

        if i == 0:

            z += 1

        else:
            
            ls.append(i)


    for i in range(z):

        ls.append(0)

    return ls


ls = [0,1,0,3,12]

print(f"Lista da modificare: {ls}")

new_ls = move_zeroes(ls)


print(f"Ecco a te la nuova lista {new_ls}")





#esercizio 5-bis

def move_zeroes_bis(nums: list[int]):

    z: int = 0

    for i in nums:

        if i == 0:

            nums.pop(i)
            nums.append(i)

    return nums


ls_bis = [0,1,0,3,12]

print(f"\n\nLista da modificare: {ls}")

new_ls_bis = move_zeroes_bis(ls)


print(f"Ecco a te la nuova lista {new_ls}")



#esercizio 6

def intersection(nums1: list[list], nums2: list[list])-> list[list]:

    set_nums1 = set(nums1)
    set_nums2 = set(nums2)
    intersection_nums: list = []

    for i in set_nums1:

        for j in set_nums2:

            if i == j:

                intersection_nums.append(i)


    return intersection_nums




ls1: list = [1,1,2,3,4,6,5,7,8]
ls2: list = [2,5,6,8,2,4,8,3,0]

intersection_ls: list = intersection(ls1,ls2)


print(intersection_ls)
