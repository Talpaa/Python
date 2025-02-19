def anagram(s: str, t: str) -> bool:

    s = s.lower()
    t = t.lower()
    stringa: list = []

    for j in s:

        stringa.append(j)

    presente: bool = True    

    for i in t:

        if i in s:

            stringa.remove(i)

        else:
            return False

    return presente

print(anagram("anagram","nagaram"))#Output True

print(anagram("rat", "car"))#Output False

print(anagram("silent","listen"))#Output True

print(anagram("NeurIPS","UniReps"))#Output True