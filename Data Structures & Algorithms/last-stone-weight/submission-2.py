class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a,b = heapq.heappop(stones), heapq.heappop(stones)
            if b>a:
                heapq.heappush(stones, a-b)
        stones.append(0)
        return abs(stones[0])