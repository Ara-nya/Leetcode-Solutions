class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        left = 0
        max_len = 0
    
        for right in range(len(nums)):
        # Add the current element to the frequency map
            current_num = nums[right]
            freq[current_num] = freq.get(current_num, 0) + 1
        
        # If the frequency exceeds k, shrink the window from the left
            while freq[current_num] > k:
                left_num = nums[left]
                freq[left_num] -= 1
                left += 1
            
        # Update the maximum length found so far
            max_len = max(max_len, right - left + 1)
        
        return max_len