
# Your previous Plain Text content is preserved below:


# Finding interesting triplet


# Given an integer array arr,
# An interesting triplet is defined as 3 indices i, j and k
# 0 <= i < j < k < len(arr)

# such that arr[i] < arr[j] < arr[k]

# Please check whether arr has at least one interesting triplet.

#           0.  1      3
# arr = [-2, -1, -5, 3]
# return True, 
# i = 0, j = 1, k = 3

# arr = [-2, -1, -5, -3]
# return False

'''
value: -5 -2 -1 3
index: 2, 0, 1, 3
           j=3
-3, -4, -5, 6, 5, 4, 3
(i = 0, j = 3)
k in range(3, n): arr[k] > arr[j] ?

(i = 1, j = 3)
k in range(3, n): arr[k] > arr[j] ?

(i = 2, j = 3)
k in range(3, n): arr[k] > arr[j] ?

For the same j value, we don't need to find k again and again.

'''

arr = [-2, -1, -5, 3]

def findInteresting(arr):
    for j in range(1, len(arr)-1):
        found_i = False
        temp = None
        for i in range(j):
            if arr[j] > arr[i]:
                found_i = True
                temp = arr[i]
        if not found_i:
            continue
        for k in range(j + 1, len(arr)):
            if temp:
                if arr[k] > arr[j] and arr[j] > temp:
                    return True
    return False

print(findInteresting(arr))

'''
1. Data structure & algorithm
2. Code style
3. Test (dry run)
4. Communication
4.1 you to interviewer
Ask clarifications
Ask hints
Ask question
Ask corner cases

4.2 interviewer to you
Provide early feedback
Confirm the idea works/doesn't work


For the same j value, we don't need to find k again and again.

Why we have duplicated j value?

(1) We still allow the duplicate, but we do something special when the same j occurs. 
We need a way to check whether a value occured before or not.
We need a data structure to insert/query values.
HashSet, set

s = set()
for i in range(n):
    for j in range(i + 1, n):
        if arr[j] > arr[i]:
            if not j in s:
                for k in range(j + 1, n):
                    if arr[k] > arr[j]:
                        return True
                s.add(j)
return False

O(n ^ 2)

(2) We don't allow duplication
for j in range(...)
   for i...
   for k..
[.....]j[.....]

O(n ^ 2)

mark = [False] * n
for i in range(n)
  for j in range(i + 1, n)
     if arr[i] < arr[j]:
        mark[i] = True

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] < arr[j] and mark[j]:
            return True
O(n ^ 2)

[...minimum..]j[..maximum..]

loop i from left to right
prefix_min[i] = min(arr[0], arr[1],...arr[i])

              = min(prefix_min[i - 1], arr[i])
prefix_min[0] = arr[0]

loop i from right to left
suffix_max[i] = max(arr[i], arr[i + 1],...arr[-1])
              = max(suffix_max[i + 1], arr[i])
suffix_max[n - 1] = arr[-1]

loop i
prefix_min[i] < arr[i] < suffix_max[i]
prefix_min[i - 1] < arr[i] < suffix_max[i + 1]

O(n)
O(n)

O(n)
O(1)
Loop all the values from left to right
1. The smallest value so far.
2. The smallest value which has a smaller value on its left so far.

(a)
(?, b)
x

a = float('inf')
b = float('inf')
for x in arr:
    if x > b:
        return True
    if x > a:
        # a < x <= b
        # (a)
        # (a, x)
        # (?, b)
        b = x
    else:
        # x <= a
        # (x)
        # (a)
        # (?, b)
        a = x
return False
    

'''
