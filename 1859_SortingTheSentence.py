class Solution:
    def sortSentence(self, s: str) -> str:
        
        words = s.split(" ")
        ans = ""
        dict_ans = {}
        
        for i in words:
            temp = int(i[len(i)-1])
            dict_ans[temp] = i[:len(i)-1]
            
        
        for i in sorted(dict_ans.keys()):
            ans += dict_ans[i] + " "
            
        ans = ans.rstrip()
        return ans
        
