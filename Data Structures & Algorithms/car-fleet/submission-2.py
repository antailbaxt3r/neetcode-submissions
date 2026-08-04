class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        data = [(p, s) for p, s in zip(position, speed)]
        data.sort(reverse=True)

        for p, s in data:
            time = (target - p) / s
            if stack and stack[-1] >= time:
                continue
            stack.append(time)

        return len(stack)

