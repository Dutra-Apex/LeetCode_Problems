class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        
        allowed = [char for char in allowed]
           
        count = 0
        
        for word in words:
            
            check = False
            
            for char in word:
                if char in allowed:
                    check = True
                else:
                    check = False
                    break
                
            if check == True:
                count += 1
                
        return count
