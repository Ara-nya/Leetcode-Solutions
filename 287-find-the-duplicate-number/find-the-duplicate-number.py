class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unordered_set = set()
        for items in nums:
            if items in unordered_set:
                return items
            else:
                unordered_set.add(items)
