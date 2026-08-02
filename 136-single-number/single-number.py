class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        XOR = 0
        for items in nums:
            XOR = XOR ^ items

        return XOR