class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        l, r = 0, len(people)-1
        people.sort()
        while l <= r:
            boat += 1
            empty = limit - people[r]
            r -= 1
            if people[l] <= empty:
                l += 1
        return boat
            