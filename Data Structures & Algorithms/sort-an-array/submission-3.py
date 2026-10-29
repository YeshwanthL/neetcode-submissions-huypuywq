class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(L, R, M, arr):
            LEFT, RIGHT = arr[L:M+1], arr[M+1:R+1]
            i, j, k = 0, 0, L
            while i < len(LEFT) and j < len(RIGHT):
                if LEFT[i] > RIGHT[j]:
                    arr[k] = RIGHT[j]
                    j += 1
                else:
                    arr[k] = LEFT[i]
                    i += 1
                k += 1
            while i < len(LEFT):
                arr[k] = LEFT[i]
                i += 1
                k += 1
            while j < len(RIGHT):
                arr[k] = RIGHT[j]
                j += 1
                k += 1
        def mergeSort(l, r, arr):
            if l < r:
                m = (l + r) >> 1
                mergeSort(l, m, arr)
                mergeSort(m+1, r, arr)
                merge(l, r, m, arr)
        mergeSort(0, len(nums)-1, nums)
        return nums