class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        total_pushes = 0
        
        # Iterate through each character's position
        for i in range(n):
            # The cost increases by 1 for every 8 characters
            cost = (i // 8) + 1
            total_pushes += cost
            
        return total_pushes