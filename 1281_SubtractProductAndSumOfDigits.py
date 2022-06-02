class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        n = str(n)
        
        sum_n = 0
        product_n = 1
        
        for i in n:
            sum_n += int(i)
            product_n *= int(i)
            
        return product_n - sum_n
