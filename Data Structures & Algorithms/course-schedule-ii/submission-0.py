class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = { i: [] for i in range(numCourses)}
        for c,p in prerequisites:
            premap[c].append(p)
        
        visiting = set()
        cycle = set()
        res = []
        def dfs(c):
            if c in visiting:
                return True
            if c in cycle:
                return False

            cycle.add(c)
            for p in premap[c]:
                if not dfs(p):
                    return False
            cycle.remove(c)
            visiting.add(c)
            res.append(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res