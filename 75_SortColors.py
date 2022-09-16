class Solution:
    def sortColors(self, nums: List[int]) -> None:
       
        count = []
        count.append(nums.count(0))
        count.append(nums.count(1))
        count.append(nums.count(2))
        index = 0
        
        for i in range(3):
            
            while count[i] > 0:
                nums[index] = i
                index += 1
                count[i] -= 1
