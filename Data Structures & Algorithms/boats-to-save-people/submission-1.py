class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        l = 0
        r = len(people) - 1
        boats = 0
        while l <= r:
            val = people[l] + people[r]
            
            if val <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            boats += 1
        return boats