class Solution:
    def mergeSort(self, l, r, m, arr):
        LEFT, RIGHT = arr[l:m+1], arr[m+1:r+1]
        i, j, k = l, 0, 0
        while j < len(LEFT) and k < len(RIGHT):
            if LEFT[j] <= RIGHT[k]:
                arr[i] = LEFT[j]
                j += 1
            else:
                arr[i] = RIGHT[k]
                k+=1
            i += 1
        while j < len(LEFT):
            arr[i] = LEFT[j]
            i+=1
            j+=1
        while k < len(RIGHT):
            arr[i] = RIGHT[k]
            i+=1
            k+=1

    def merge(self, l, r, nums):
        if l == r:
            return
        m = (l+r) >> 1
        self.merge(l, m,nums)
        self.merge(m+1, r, nums)
        self.mergeSort(l, r, m ,nums)
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge(0, len(nums)-1, nums)
        return nums
        