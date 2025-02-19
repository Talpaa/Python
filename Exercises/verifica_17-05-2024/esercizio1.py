def word_break(s: str, wordDict: list[str]) -> bool:

    presente: bool = False
    stringa: str = wordDict[0]
    
    for i in wordDict[1:]:

        stringa += i

        
    if len(s) >= len(stringa):
        for i in wordDict:

            if i in s:

                presente = True

            else:

                return False
        
    return presente

print(word_break("leetcode",["leet","code"]))#Output True

print(word_break("applepenapple", ["apple","pen"]))#Output True

print(word_break("catsandog",["cats","dog","sand","and","cat"]))#Output False