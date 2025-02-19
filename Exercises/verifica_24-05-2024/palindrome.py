'''
Given a string s which consists of lowercase or uppercase letters, 
write a function that returns the length of the longest palindrome that can be built with those letters. 
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
'''

def longest_palindrome(s: str) -> int:

    dizionario: dict = {}
    
    lun_par: int = 0

    count: int = 0

    for char in s:

        if char in dizionario:

            dizionario[char] += 1

        else:

            dizionario[char] = 1

    for key in dizionario:

        if (dizionario[key] % 2) == 0:

            lun_par += dizionario[key]

        elif ((dizionario[key] % 2) == 1)and(dizionario[key] > 2):

            lun_par += dizionario[key]-1
            count += 1

        elif (dizionario[key] > 0)and(dizionario[key] < 2):

            count += 1


    if count >0:

        lun_par += 1


    print(dizionario)
    return lun_par

        


print(longest_palindrome("abcabcabc")) #Output 7