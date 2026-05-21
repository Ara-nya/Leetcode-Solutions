class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for items in s:
            if items in "({[":
                stack.append(items)
            else:
                if not stack or mapping[items] != stack.pop():
                    return False
        return len(stack) == 0