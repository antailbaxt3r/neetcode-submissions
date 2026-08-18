class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            s_s = str(sorted(s))
            hashmap[s_s].append(s)
        return list(hashmap.values())