class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for st in strs:
            stCount = [0]*26

            for s in st:
                stCount[ord(s)-ord('a')]+=1
            
            res[tuple(stCount)].append(st)
        
        return res.values()
            