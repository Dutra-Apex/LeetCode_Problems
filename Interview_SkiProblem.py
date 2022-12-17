# # Ski problem

# There is a 2D array m*n matrix that represents the top view of a ski area

# 1   2  3  4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

# 6 1 2
# 1 4 3

# Each number represents the height of that location.
# David likes skiing, because he enjoys the time of skiing from the top to the bottom.
# But he hates the time of climbing up from the bottom to the top.
# So he always tries to find the longest path to ski in the mountain area.

# In this ski area, he can choose any location as the start point and ski to the neighbor location in a direction of up, down, left, right, if the next location is lower than the current location.

# Let’s help him to find the longest path for skiing.
# Return the length of the longest path.

# return the length of longest path starting from i, j
def helper(grid, i, j):

    path_len = 1
    # if (j <= 0 and i <= 0) or (j >= len(grid[0]) and i >= len(grid[1])):
    #     return path_len
    
    temp1, temp2, temp3, temp4, = 0,0,0,0
    if i-1 >= 0  and grid[i-1][j] < grid[i][j]:
        temp1 += helper(grid, i-1, j) 
    if (i+1 <= len(grid)-1) and grid[i+1][j] < grid[i][j]:
        temp2 += helper(grid, i+1, j) 
    if j-1 >= 0 and grid[i][j-1] < grid[i][j]:
        temp3 += helper(grid, i, j-1) 
    if j+1 <= len(grid)-1 and grid[i][j+1] < grid[i][j]:
        temp4 += helper(grid, i, j+1)

    return path_len + max(temp1, max(temp2, max(temp3, temp4)))



def find_longest_path(grid):
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            temp = helper(grid, i, j)
            if temp > ans:
                ans = temp
    return ans

a = [[1 ,  2,  3,  4, 5],
 [16, 17, 18, 19, 6],
 [15, 24, 25, 20, 7],
 [14, 23, 22, 21, 8],
 [13, 12, 11, 10, 9]]

print(find_longest_path(a))
