class Solution:
    def majorityElement(self, nums: List[int]) -> int:       
        prev = []

        for i in nums:
            if i not in prev:
                prev.append(i)
                
                if nums.count(i) > (len(nums)//2):
                    return i
