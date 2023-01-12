class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def check_self_divide(num):
            temp = str(num)
            if '0' in temp:
                return False
            for i in temp:
                if num % int(i) != 0:
                    return False
            return True

        ans = []
        for i in range(left, right+1):
            if check_self_divide(i):
                ans.append(i)

        return ans
