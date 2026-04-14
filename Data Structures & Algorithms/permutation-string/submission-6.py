class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1)>len(s2):
            return False
        
        countS1=[0]*26
        countS2=[0]*26

        size=len(s1)

        for i in range(len(s1)):
            countS1[ord(s1[i])-ord('a')]+=1
            countS2[ord(s2[i])-ord('a')]+=1
        
        matches=26

        for i in range(26):
            if countS1[i] != countS2[i]:
                matches-=1
        
        l=0

        for r in range(size,len(s2)):

            if matches==26:
                return True
            
            idx = ord(s2[r])-ord('a')
            countS2[idx]+=1

            if countS1[idx]==countS2[idx]:
                matches+=1
            elif countS1[idx]+1 == countS2[idx]:
                matches-=1

            idx = ord(s2[l])-ord('a')
            countS2[idx]-=1

            if countS1[idx]==countS2[idx]:
                matches+=1
            elif countS1[idx]-1 == countS2[idx]:
                matches-=1
            l+=1
        return matches==26


            
