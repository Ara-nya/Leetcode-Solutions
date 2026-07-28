class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        store = {}
        seen_values = set()
        
        for i in range(len(s)):
            char1 = s[i]
            char2 = t[i]
            
            if char1 in store:
                if store[char1] != char2:
                    return False  
            else:
                if char2 in seen_values:
                    return False  
                    
                store[char1] = char2
                seen_values.add(char2)
                
        return True