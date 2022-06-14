class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.split(' ')
        
        i = 1
        while len(s[-i]) == 0:
            i += 1
            
        return len(s[-i])
