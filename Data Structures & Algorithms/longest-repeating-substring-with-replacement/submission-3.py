class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        maxf = 0

        l = 0
        store = {}
        for r in range(len(s)):
            store[s[r]] = store.get(s[r], 0) + 1
            maxf = max(maxf, store[s[r]])
            if (r-l+1) - maxf > k:
                store[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res