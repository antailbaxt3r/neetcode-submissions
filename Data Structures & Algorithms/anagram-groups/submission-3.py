class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            count = [0 for _ in range(26)]
            for i in s:
                count[ord(i) - ord('a')] += 1
            count = tuple(count)
            if count in groups:
                groups[count].append(s)
            else:
                groups[count] = [s]
        return list(groups.values())