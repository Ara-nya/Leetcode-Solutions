class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r, zeroes, maxLen = 0, 0, 0, 0
        while r < len(nums):
            if nums[r] == 0:
                zeroes += 1
            if zeroes > k:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1
            if zeroes <= k:
                curr_len = r-l+1
                maxLen = max(maxLen, curr_len)
            r += 1
        return maxLen