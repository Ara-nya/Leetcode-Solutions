class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split() 
        if len(pattern) != len(words):
            return False
            
        store = {}
        seen_value = set()
        
        for i in range(len(pattern)):
            char1 = pattern[i]
            char2 = words[i]
            
            if char1 in store:
                if store[char1] != char2:
                    return False
            else:
                if char2 in seen_value:
                    return False
                store[char1] = char2
                seen_value.add(char2)

        return True