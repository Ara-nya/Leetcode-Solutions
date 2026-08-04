class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # missing = []

        # n = len(nums)
        # first = nums[0]
        # last = nums[n-1]
        
        
        # for i in range (first, last):
        #     if i in nums:
        #         continue
        #     else:
        #         missing.append(i)
        
        # return missing



        if not nums:
            return []
            
        # Converting to a set
        num_set = set(nums)
        missing = []
        
        first = min(nums)
        last = max(nums)
        
        for i in range(first, last):
            if i not in num_set:
                missing.append(i)
                
        return missing