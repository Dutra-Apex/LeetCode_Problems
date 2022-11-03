import math 
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        occ_seats = [0]     
        for i in range(1, len(seats) -1):
            if seats[i] == 1:
                occ_seats.append(i)
                
        occ_seats.append(len(seats)-1)              
        max_dist = 0
        temp = 0
        
        for j in range(len(occ_seats)-1):   
            temp = abs((occ_seats[j]-occ_seats[j+1])/2)
            temp = math.floor(temp)
            
            if j == (len(occ_seats) - 2):
                if seats[-1] == 0:
                    temp = abs((occ_seats[j]-occ_seats[j+1])) 
            if j == 0:
                if seats[0] == 0:
                    temp = abs((occ_seats[j]-occ_seats[j+1]))
                    
            if temp >= max_dist:
                max_dist = temp
                
        return max_dist
