class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(l,m, r, nums):
            LEFT, RIGHT = nums[l:m+1], nums[m+1:r+1]
            i,j, k =l,0,0

            while j < len(LEFT) and k < len(RIGHT):
                if LEFT[j] < RIGHT[k]:
                    nums[i] = LEFT[j]
                    j += 1
                else:
                    nums[i] = RIGHT[k]
                    k += 1
                i += 1
            
            while j < len(LEFT):
                nums[i] = LEFT[j]
                j += 1
                i += 1

            while k < len(RIGHT):
                nums[i] = RIGHT[k]
                k += 1
                i += 1

        def mergeSort(l, r, nums):
            if l == r:
                return
            m = (l+r) >> 1
            mergeSort(l,m, nums)
            mergeSort(m+1,r,nums)
            merge(l,m,r,nums)
        mergeSort(0, len(nums)-1, nums)
        return nums