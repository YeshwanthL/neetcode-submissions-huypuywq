class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_store = [0] * 26
        s2_store = [0] * 26

        for i in range(len(s1)):
            s1_store[ ord(s1[i]) - ord('a') ] += 1
            s2_store[ ord(s2[i]) - ord('a') ] += 1
        
        matches = 0
        for i in range(26):
            if s1_store[i] == s2_store[i]:
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            cur =  ord(s2[l])-ord('a')
            l += 1
            s2_store[cur] -= 1
            if s2_store[cur]  == s1_store[cur]-1:
                matches -= 1
            elif s2_store[cur] == s1_store[cur]:
                matches += 1
            
            cur = ord(s2[r])-ord('a') 
            s2_store[cur] += 1

            if s1_store[cur] + 1 == s2_store[cur]:
                matches -= 1
            elif s2_store[cur]  == s1_store[cur]:
                matches += 1
        
        return matches == 26