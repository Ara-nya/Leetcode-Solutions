class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        temp = word
        count = 0
        if temp not in sequence:
            return 0
        while temp in sequence:
            count += 1
            temp = temp+word

        return count