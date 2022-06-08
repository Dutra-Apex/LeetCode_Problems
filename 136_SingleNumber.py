class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans = 0
        
        # The '^=' operator is XOR
        # XOR of 0 and n returns n
        # XOR of n and n returns 0
        
        for num in nums:
            ans ^= num
            
        return ans
