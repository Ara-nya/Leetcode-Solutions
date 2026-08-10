class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] represents if the current player can win with i stones remaining
        dp = [False] * (n + 1)
        
        # Calculate winning states bottom-up
        for i in range(1, n + 1):
            k = 1
            # Try removing all possible square numbers of stones <= i
            while k * k <= i:
                # If this move leaves the opponent in a losing state, 
                # then i is a winning state for the current player.
                if not dp[i - k * k]:
                    dp[i] = True
                    break # We found a winning move, no need to check further
                k += 1
                
        # Return the state for n stones (Alice's starting position)
        return dp[n]