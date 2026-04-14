class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        res=0
        while l<r:
            length= abs(l-r)*min(heights[l],heights[r])
            res=max(res,length)
            if(heights[l]<heights[r]):
                l+=1
            elif heights[r] <= heights[l]:
                r -= 1    
        return res