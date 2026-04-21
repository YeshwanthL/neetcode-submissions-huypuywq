class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        store = defaultdict(int)
        maxf = 0
        res = 0
        for r in range(len(s)):
            store[s[r]] += 1
            maxf = max(maxf, store[s[r]])
            if (r-l+1) - maxf > k:
                store[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res

