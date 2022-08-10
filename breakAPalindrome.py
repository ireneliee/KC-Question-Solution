def breakPalindrome(palindromeStr):
    
    #function to check whether it's a palindrome or not
    def isAPalindrome(word):
        for i in range(len(word)):
            if word[i] != word[len(word) - 1 - i]:
                return False
    
    reformedWord = None
    for i in range(len(palindromeStr)):
        if 98 <= ord(palindromeStr[i]) <= 122:
            reformedWord = palindromeStr[:i] + chr(ord(palindromeStr[i]) - 1) + palindromeStr[i + 1:]
            if isAPalindrome(reformedWord) == False:
                return reformedWord
    
    return "IMPOSSIBLE"

print(breakPalindrome("aaaabaaa"))


    
    

breakPalindrome("xx")

