class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1
        size = len(numbers)
        while l != r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            else:
                r -= 1 
