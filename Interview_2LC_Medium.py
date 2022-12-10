'''
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.
 

Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step.

'''

'''
loop through string 
    i        i
s="abc"  t="ab"

'''
def can_edit(s, t):

    if s == t:
        return False

    if len(t) > (len(s) + 1) or len(s) > (len(t) + 1):
        return False

    curr = ""
    if len(s) > len(t):
        curr = t
    else: 
        curr = s

    n_different = 0            ### s=ab  t=abb
    for i in range(len(curr)):
        if s[i] != t[i]:
            n_different += 1

    if (n_different == 1 and len(t) == len(s)) or n_different == 0:
        return True 
    
    return False


s = ""
t = "cv"
print(can_edit(s, t))


'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

1, 1
0, 1
2, 1
1, 0
1, 2


Input: grid = [
  ["1","1","0","0","0"],
  ["1",1"","0","0","0"],
  ["1","1","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

hint: 
Hint: r, c 

 r+1, c
 r,c+1
 r-1, c
 r, c-1 

'''

'''

'''

def helper(grid, i, j):
    isIsland = True

    if i < 0 or j < 0 or i > (len(grid)-1) or j > (len(grid)-1):
        return False

    if grid[i][j] == 1:
        grid[i][j] = '0'

    for sid in [(i+1, j),(),(),()]
        helper(grid, sid[0], sid[i]),


    return False


