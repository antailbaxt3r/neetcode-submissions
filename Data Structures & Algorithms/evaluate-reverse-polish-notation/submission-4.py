class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x == "+":
                stack.append(stack.pop() + stack.pop())
            elif x == "*":
                stack.append(stack.pop() * stack.pop())
            elif x == '-':
                stack.append(-1 * stack.pop() + stack.pop())
            elif x == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(x))
        return stack.pop()