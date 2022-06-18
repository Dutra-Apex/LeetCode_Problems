class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        ans = [1 for k in range(len(ratings))]
        
        for i in range(0, len(ratings) - 1):
            if ratings[i+1] > ratings[i]:
                ans[i+1] = ans[i]+1
                
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j+1] < ratings[j]:
                ans[j] = max(ans[j+1]+1, ans[j])
            
        return sum(ans)
