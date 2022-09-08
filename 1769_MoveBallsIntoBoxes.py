class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        answer = []
        ball_pos = []
        min_ops = 0
        
        for i in range(len(boxes)):
            
            if boxes[i] == '1':
                ball_pos.append(i)
                
        for i in range(0, len(boxes)):
            
            for j in ball_pos:
                
                min_ops += abs(i-j)
            
            answer.append(min_ops)
            min_ops = 0
                
        return answer
