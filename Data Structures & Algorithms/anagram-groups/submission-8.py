class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)

        for s in strs:
            temp = [0] * 26
            for i in range(len(s)):
                temp[ ord(s[i]) - ord('a') ] += 1
            store[tuple(temp)].append(s)
        
        res = []

        for k,v in store.items():
            res.append(v)
        
        return res
            

        