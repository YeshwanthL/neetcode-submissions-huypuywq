class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(a,b):
            while a<b:
                if s[a] != s[b]:
                    return False
                a += 1
                b -= 1
            return True

        l,r = 0,len(s)-1
        while l<r:
            if s[l] != s[r]:
                return (isPalindrome(l+1,r) or isPalindrome(l,r-1))
            l += 1
            r -=1
        return True
        