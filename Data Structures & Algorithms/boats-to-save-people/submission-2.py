class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        l, r = 0, len(people)-1
        people.sort()
        while l <= r:
            boats += 1
            empty_seat = limit - people[r]
            r -= 1
            if people[l] <= empty_seat:
                l += 1
        return boats
