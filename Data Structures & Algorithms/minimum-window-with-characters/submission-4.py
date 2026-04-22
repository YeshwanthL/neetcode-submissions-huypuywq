class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        s_store = {}
        t_store = {}

        for c in t:
            t_store[c] = t_store.get(c, 0) + 1
        
        have, need = 0,len(t_store)
        res, resLen = [-1, -1], float("infinity")

        l = 0
        for r in range(len(s)):
            c = s[r]
            s_store[c] = s_store.get(c, 0) + 1
            if c in t_store and t_store[c] == s_store[c]:
                have += 1
            
            while have == need:
                if r-l+1 < resLen:
                    res = [l, r]
                    resLen = r-l+1

                s_store[s[l]] -= 1
                if s[l] in t_store and t_store[s[l]] -1 == s_store[s[l]]:
                    have -=1 
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""
