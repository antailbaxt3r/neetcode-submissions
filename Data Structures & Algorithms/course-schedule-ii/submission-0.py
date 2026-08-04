class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = [0] * numCourses
        q = collections.deque()
        
        adj = [[] for _ in range(numCourses)]
        for [x, y] in prerequisites:
            adj[x].append(y)
            degree[y] += 1
        
        for i in range(numCourses):
            if degree[i] == 0:
                q.append(i)

        answer = []
        while q:
            node = q.popleft()
            answer = [node] + answer
            for n in adj[node]:
                degree[n] -= 1
                if degree[n] == 0:
                    q.append(n)
        if len(answer) == numCourses:
            return answer
        return []
        
