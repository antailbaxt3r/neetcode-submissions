class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        comp = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for c in s:
            if c in comp:
                if not stack or stack.pop() != comp[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0