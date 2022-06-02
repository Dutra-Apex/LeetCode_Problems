class Solution:
    def isHappy(self, n: int) -> bool:
        
        sum_n = 0
        n_list = []
        
        while n != 1:
            
            if n in n_list:
                return False
            
            n_list.append(sum_n)
            sum_n = 0
            
            for i in str(n):
                sum_n += int(i) * int(i)
            
            n = sum_n
            
        return True
