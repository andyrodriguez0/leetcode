
from __future__ import annotations

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # MergeSort

        # def merge(list1, list2):

        #     list3 = []
        #     i = j = 0

        #     while i < len(list1) and j < len(list2):
        #         if list1[i] <= list2[j]:
        #             list3.append(list1[i])
        #             i += 1
        #         else:
        #             list3.append(list2[j])
        #             j += 1
            
        #     while i < len(list1):
        #         list3.append(list1[i])
        #         i += 1
            
        #     while j < len(list2):
        #         list3.append(list2[j])
        #         j += 1
            
        #     return list3

        # def mergesort(list1):

        #     if len(list1) == 1:
        #         return list1
            
        #     mid = len(list1) // 2
        #     left = mergesort(list1[:mid])
        #     right = mergesort(list1[mid:])
        #     list2 = merge(left, right)

        #     return list2
        
        # return mergesort(nums)

        # InsertionSort

        # for i in range(1, len(nums)):

        #     key = nums[i]
        #     j = i - 1
            
        #     while j > -1 and nums[j] > key:
        #         nums[j + 1] = nums[j]
        #         j -= 1
            
        #     nums[j + 1] = key
        
        # return nums

        # QuickSort

        def partition(list1, p, r):

            key = list1[r]
            i = p - 1

            for j in range(p, r):

                if list1[j] <= key:
                    i += 1
                    list1[i], list1[j] = list1[j], list1[i]

            list1[i + 1], list1[r] = list1[r], list1[i + 1]

            return i + 1
        
        def quicksort(list1, p, r):

            if p < r:
                q = partition(list1, p, r)
                quicksort(list1, p, q - 1)
                quicksort(list1, q + 1, r)
        
        quicksort(nums, 0, len(nums) - 1)

        return nums

solution = Solution()
print(solution.sortArray([5,1,1,2,0,0]))