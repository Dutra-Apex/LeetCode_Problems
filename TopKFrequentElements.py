class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        f_map = {}
        ans = []

        for num in nums:
            try:
                f_map[num] += 1
            except:
                f_map[num] = 1

        f_map = sorted(f_map.items(), key=lambda x:x[1], reverse = True)

        for i in range(k):
            ans.append(f_map[i][0])

        return ans
