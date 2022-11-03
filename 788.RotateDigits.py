class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        def validateRotation(num):
            num = str(num)
            num_list = []
            good = False
            list_good = ['2', '5', '6', '9']
            list_valid = ['0', '1', '8']
            
            for i in num:
                if i in list_valid:
                    num_list.append(False)
                elif i in list_good:
                    num_list.append(True)
                else:
                    return False
                
            if True in num_list:
                return True
            return False
                    
        ans = 0
        
        for i in range(n+1):
            if validateRotation(i):
                ans += 1
                
        return ans
