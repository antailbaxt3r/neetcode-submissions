class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        inOrder = sorted([(p, s) for p, s in zip(position, speed)])
        stack = []
        for p, s in inOrder:
            t = (target-p) / s
            while stack and t >= stack[-1]:
                stack.pop()
            stack.append(t)
        return len(stack)