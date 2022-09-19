class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
       
        listPos = []
        hasZero = False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    listPos.append(j)
                    hasZero = True
            if hasZero == True:
                matrix[i] = [0] * len(matrix[i])
                hasZero = False
                
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j in listPos:
                    matrix[i][j] = 0
