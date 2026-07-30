class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        score = 0
        for num in nums:
            if score == 0:
                candidate = num

            if num == candidate:
                score += 1
            else:
                score -= 1
            
        return candidate