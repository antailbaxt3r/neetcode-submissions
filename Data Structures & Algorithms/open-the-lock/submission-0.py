class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        q = deque()
        q.append(("0000", 0))
        visited = set(deadends)

        while q:
            n, t = q.popleft()
            if n == target:
                return t
            
            options = []
            for i in range(4):
                digit = str((int(n[i]) + 1) % 10)
                options.append(n[:i] + digit + n[i+1:])
                digit = str((int(n[i]) + 9) % 10)
                options.append(n[:i] + digit + n[i+1:])                

            for c in options:
                if c not in visited:
                    visited.add(c)
                    q.append((c, t+1))
        
        return -1
