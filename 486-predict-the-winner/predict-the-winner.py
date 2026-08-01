class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # dp[i] represents the maximum score difference a player can achieve 
        # against their opponent for the subarray starting at index i.
        # Initially, for subarrays of length 1, the difference is just the number itself.
        dp = nums[:]
        
        # Build the solution for subarrays of length 2 up to n
        for length in range(2, n + 1):
            # i is the starting index of the subarray
            for i in range(n - length + 1):
                j = i + length - 1
                
                # The current player has two choices:
                # 1. Take the left element (nums[i]) and subtract the opponent's best future difference (dp[i+1])
                # 2. Take the right element (nums[j]) and subtract the opponent's best future difference (dp[i])
                dp[i] = max(nums[i] - dp[i + 1], nums[j] - dp[i])
                
        # If the max score difference for the entire array (nums[0...n-1]) is >= 0, Player 1 wins
        return dp[0] >= 0