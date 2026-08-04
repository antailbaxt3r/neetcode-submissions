class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(s, i, j, flag):
            while i < j:
                if not s[i].isalnum():
                    i += 1
                elif not s[j].isalnum():
                    j -= 1
                elif s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                elif flag:
                    return False
                else:
                    return isValid(s, i+1, j, True) or isValid(s, i, j-1, True)
            return True
        
        n = len(s)
        i = 0
        j = n-1

        return isValid(s, i, j, False)
                