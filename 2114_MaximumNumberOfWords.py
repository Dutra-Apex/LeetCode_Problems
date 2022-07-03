class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        c = 1
        ans = 0
        
        for i in sentences:
            for j in i:
                if j == " ":
                    c += 1
            if c > ans:
                ans = c
            c = 1
        
        return ans
