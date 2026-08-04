class Solution:
    def isValid(self, s: str) -> bool:
        comp = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        stack = []
        for c in s:
            if c in comp:
                stack.append(c)
            elif len(stack) > 0 and c == comp[stack[-1]]:
                stack = stack[:-1]
            else:
                return False
        return len(stack) == 0