class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_map = {}

        for t in tasks:
            count_map[t] = count_map.get(t, 0) + 1
        
        max_heap = [ -c for c in count_map.values()]
        heapq.heapify(max_heap)
        q = deque()
        t = 0

        while max_heap or q:
            t += 1
            if not max_heap:
                t = q[0][1]
            else:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, t+n])
            if q and q[0][1] == t:
                heapq.heappush(max_heap, q.popleft()[0])
        return t
