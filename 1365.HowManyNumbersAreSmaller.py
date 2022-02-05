class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        for i in nums:
            counter = 0  
            
            for j in nums:
                
                if j < i:
                    counter += 1
                    
            ans.append(counter)
            
        return ans
