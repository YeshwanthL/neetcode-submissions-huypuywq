class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            tmp = [0] * 26
            for c in s:
                tmp[ ord(c) - ord('a') ] += 1
            group[tuple(tmp)].append(s)
        
        res = []
        for k,v in group.items():
            res.append(v)
        return res