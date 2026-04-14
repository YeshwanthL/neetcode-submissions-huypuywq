class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        # countS,countT={},{}

        # for i in range(len(s)):
        #     countS[s[i]] = 1+ countS.get(s[i],0)
        #     countT[t[i]] = 1+ countT.get(t[i],0)
        
        # return countS==countT

        res = [0]*26

        for i in range(len(s)):
            res[ord(s[i])-ord('a')]+=1
            res[ord(t[i])-ord('a')]-=1
        
        for n in res:
            if n!=0:
                return False
        return True