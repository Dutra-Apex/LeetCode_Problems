class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def permute(nums, perm = [], res = []):

            if not nums:
                if perm not in res:
                    res.append(perm)
            for i in range(len(nums)):
                newNums = nums[:i] + nums[i+1:]
                newPerm = perm + [nums[i]]
                permute(newNums, newPerm, res)
            return res

        return(permute(nums))
