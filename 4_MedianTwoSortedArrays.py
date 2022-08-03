class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums3 = nums1 + nums2
        nums3 = sorted(nums3)
        len_nums3 = len(nums3)
        median_index = len_nums3//2

        if len_nums3 < 2:
            return nums3[0]
        elif len_nums3 % 2 != 0:
            return nums3[median_index]
        else:
            return (nums3[median_index] + nums3[median_index -1])/2
