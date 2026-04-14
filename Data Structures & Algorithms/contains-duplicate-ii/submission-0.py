class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store = {}

        for i,n in enumerate(nums):
            if n in store:
                j = store[n]
                if abs(i-j) <= k:
                    return True
            store[n] = i
        return False
