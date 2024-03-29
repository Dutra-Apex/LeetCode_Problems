class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '[':
                stack.append(']')
            elif c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif len(stack) == 0 or stack.pop() != c:
                return False

        if len(stack) == 0:
            return True
        return False
