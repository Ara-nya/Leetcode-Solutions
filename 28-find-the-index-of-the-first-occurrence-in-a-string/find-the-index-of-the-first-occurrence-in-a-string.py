class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the slice matches the needle
            if haystack[i : i + len(needle)] == needle:
                return i
        
        # If we finish the loop and never found the needle, return -1
        return -1
        