class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = 0
        min_heap = []
        for n in nums:
            heapq.heappush(min_heap, n)
        
        n = len(nums)-k

        while n != 0:
            heapq.heappop(min_heap)
            n -= 1
        return min_heap[0] 