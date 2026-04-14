class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        store_1 = [0] * 26
        store_2 = [0] * 26

        for i in range(len(s1)):
            store_1[ord(s1[i]) - ord('a')] += 1
            store_2[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            if store_1[i] == store_2[i]:
                matches += 1
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            idx = ord(s2[r]) - ord('a')
            store_2[idx] += 1

            if store_1[idx] == store_2[idx]:
                matches += 1
            elif store_1[idx]+1 == store_2[idx]:
                matches -= 1
            
            idx = ord(s2[l]) - ord('a')
            store_2[idx] -= 1

            if store_1[idx] == store_2[idx]:
                matches += 1
            elif store_1[idx]-1 == store_2[idx]:
                matches -= 1
            l += 1
        return matches == 26