class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sList = [0] * 26
        tList = [0] * 26

        for i,c in enumerate(s):
            sList[ ord('a') - ord(s[i]) ] += 1
            tList[ ord('a') - ord(t[i]) ] += 1
        return sList == tList