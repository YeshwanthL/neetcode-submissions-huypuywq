class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        store = defaultdict(int)
        cur = 0
        res = 0
        for n in nums:
            store[cur] += 1
            cur += n
            res += store[cur-k]
        return res
