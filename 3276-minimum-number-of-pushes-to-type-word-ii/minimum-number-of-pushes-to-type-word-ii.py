class Solution:
    def minimumPushes(self, word: str) -> int:
        freq_map = Counter(word)
        
        sorted_freqs = sorted(freq_map.values(), reverse=True)
        
        total_pushes = 0
        
        for i, count in enumerate(sorted_freqs):
            cost_per_push = (i // 8) + 1
            
            total_pushes += count * cost_per_push
            
        return total_pushes