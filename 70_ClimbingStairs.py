class Solution:
    def climbStairs(self, n: int) -> int:

        def fib(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            else:
                return fib(n-1) + fib(n-2)

        return fib(n)

# Mathematical Approach:
    
class Solution:
    def climbStairs(self, n: int) -> int:
        
        phi = (1 + sqrt(5))/2
        phi_ = (1 - sqrt(5))/2
        ans = ((phi**(n+1) - phi_**(n+1))/sqrt(5))
        return int(ans)
