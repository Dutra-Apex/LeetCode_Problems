class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        answer = []
        temp = 0
        
        for circle in queries:
            for point in points:
                
                a = circle[0] - point[0]
                b = circle[1] - point[1]
                c_sq = a*a + b*b
                
                if c_sq <= (circle[2] * circle[2]):
                    temp += 1
                
            answer.append(temp)
            temp = 0
            
        return answer
