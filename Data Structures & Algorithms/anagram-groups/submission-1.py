class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            freq = [0] * 26
            for c in i:
                freq[ord(c) - ord('a')] += 1
            freq = tuple(freq)
            if freq in hashmap:
                hashmap[freq].append(i)
            else:
                hashmap[freq] = [i]
        return list(hashmap.values())