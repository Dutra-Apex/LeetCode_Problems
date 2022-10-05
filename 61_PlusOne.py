class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits[-1] += 1
        c = -1
        while 10 in digits:
            if digits[c] == 10:
                digits[c] = 0
                try:
                     digits[c-1] += 1
                except:
                     digits.insert(0, 1)
            c -= 1

        return digits
