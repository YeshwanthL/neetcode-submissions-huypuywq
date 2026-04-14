class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            if s[r] in count and count[s[r]] > 0:
                while s[r] in count and count[s[r]] > 0:
                    count[s[l]] -= 1
                    l += 1
            count[s[r]] = 1
            res = max(res, r - l + 1)

        return res