class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_table = [-1] * 256
        n = len(s)
        l = 0
        r = 0
        maxLen = 0
        
        while r < n:
            char_code = ord(s[r])
            
            if hash_table[char_code] != -1:
                if hash_table[char_code] >= l:
                    l = hash_table[char_code] + 1
                    
            current_len = r - l + 1
            maxLen = max(current_len, maxLen)
            
            hash_table[char_code] = r
            r += 1
            
        return maxLen