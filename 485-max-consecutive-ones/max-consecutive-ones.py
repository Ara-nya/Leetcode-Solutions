class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLen, count = 0, 0
        for r in nums:
                if r == 1:
                    count += 1
                    maxLen = max(count, maxLen)
                else: 
                    count = 0
        return maxLen        