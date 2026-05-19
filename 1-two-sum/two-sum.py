class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range (len(nums)):
            a = nums[i]
            more = target - a
            if more in hash:
                return [hash[more], i]
            hash[a] = i
        return []