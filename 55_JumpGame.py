class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        truePath = [0] * len(nums)
        truePath[0] = 1
        
        for i in range(len(nums)-1):
            try:
                truePath[i+1:i+nums[i]+1] = [1] * (nums[i])
            except:
                continue

        if 0 in truePath:
            return False
        return True
