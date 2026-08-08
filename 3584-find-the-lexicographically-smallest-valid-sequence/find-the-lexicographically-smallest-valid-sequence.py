class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        # last[j] will store the maximum index i in word1 where 
        # word2[j...] can still be formed as a subsequence.
        last = [-1] * m
        i, j = n - 1, m - 1
        
        # Pass 1: Greedily match from right to left
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1
            
        ans = []
        canSkip = True
        j = 0
        
        # Pass 2: Greedily build the lexicographically smallest sequence from left to right
        for i in range(n):
            if j == m:
                break
                
            # Take the match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
                
            # Use our 1 allowed mismatch if the rest of the string can still be matched
            elif canSkip and (j == m - 1 or i < last[j + 1]):
                canSkip = False
                ans.append(i)
                j += 1
                
        # If we successfully matched the entirety of word2, return the sequence
        return ans if j == m else []