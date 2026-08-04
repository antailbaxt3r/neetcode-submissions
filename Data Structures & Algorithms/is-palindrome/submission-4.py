class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == " " or not s[l].isalnum():
                l += 1
            elif s[r] == " " or not s[r].isalnum():
                r -= 1
            elif s[l].lower() != s[r].lower():
                print(l, r, s[l], s[r])
                return False
            else:
                l += 1 
                r -= 1
        return True
