class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashlist = {}
        for s in strs:
            count = [0 for _ in range(26)]
            for i in s:
                count[ord(i) - ord('a')] += 1
            count = tuple(count)
            if count in hashlist:
                hashlist[count].append(s)
            else:
                hashlist[count] = [s]
        return list(hashlist.values())
