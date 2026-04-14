class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        store = {0:1}
        curr = 0
        res = 0
        for n in nums:
            curr += n
            diff = curr-k
            if diff in store:
                res += store[diff]
            store[curr] = store.get(curr,0) + 1
        return res
        