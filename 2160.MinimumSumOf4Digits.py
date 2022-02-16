class Solution:
    def minimumSum(self, num: int) -> int:
        
        arr = [int(i) for i in str(num)]
        arr = sorted(arr)
        
        return (int(str(arr[0]) + str(arr[2])) + int(str(arr[1]) + str(arr[3])))
