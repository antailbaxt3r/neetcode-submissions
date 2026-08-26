class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for s, d in prerequisites:
            degree[d] += 1
            adj[s].append(d)

        q = deque()
        for n in range(numCourses):
            if degree[n] == 0:
                q.append(n)
        count = 0
        while q:
            node = q.popleft()
            count += 1
            for n in adj[node]:
                degree[n] -= 1
                if degree[n] == 0:
                    q.append(n)
        return count == numCourses