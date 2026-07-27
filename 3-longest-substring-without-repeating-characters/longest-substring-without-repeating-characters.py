class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l, maxLen = 0, 0
        
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            
            current_len = r - l + 1
            maxLen = max(current_len, maxLen)
            seen[char] = r
            
        return maxLen
            
        return maxLen