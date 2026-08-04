class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            if not s[i].isalnum() or s[i] == ' ':
                i += 1
                continue
            if not s[j].isalnum() or s[i] == ' ':
                j -= 1
                continue
                
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True