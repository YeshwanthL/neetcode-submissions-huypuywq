class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        l = 0
        r = len(people)-1
        people.sort()
        while l <= r:
            cur = limit - people[r]
            res += 1
            r -= 1
            if l<=r and people[l] <= cur:
                l += 1
        return res