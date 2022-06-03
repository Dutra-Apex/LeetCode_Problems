class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        ans = 0
        temp = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
                
            temp = min(height[left], height[right]) * abs(right-left)
                
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
            if temp > ans:
                ans = temp
                
        return ans
