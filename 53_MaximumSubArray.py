class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        recurrentTotal = 0
        maxTotal = -10**(4)
        
        for i in nums:
            
            recurrentTotal += i
            maxTotal = max(maxTotal, recurrentTotal)
              
            if recurrentTotal <= 0:
                recurrentTotal = 0
                    
        return maxTotal
