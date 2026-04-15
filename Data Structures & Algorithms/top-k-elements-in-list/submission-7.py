class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for n in nums:
            store[n] = store.get(n, 0) + 1
        
        bucket  = [ [] for _ in range(len(nums)+1)]

        for key,v in store.items():
            bucket[v].append(key)

        res = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res