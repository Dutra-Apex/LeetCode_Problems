class Solution:
    def maxProfit(self, prices: List[int]) -> int:
          
        if len(prices) < 2:
            return 0
        
        profit = 0
        left = 0
        right = 1
            
        while right < len(prices):
            
            if prices[right] - prices[left] > profit:
                profit = prices[right] - prices[left]
            
            if prices[left] > prices[right]:
                left = right
                
            right += 1
            
        return profit
