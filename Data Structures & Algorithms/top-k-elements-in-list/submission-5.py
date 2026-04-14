class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res=[]
        countMap = defaultdict(list)

        for n in nums:
            countMap[n]=1+countMap.get(n,0)
        
        bucket=[[] for i in range(len(nums)+1)]

        for item,value in countMap.items():
            bucket[value].append(item)
        
        for i in range(len(bucket)-1,-1,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res)==k:
                    return res
