class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        elements = set()
        for i in range(n):
            for j in range(i + 1, n):
                hash_set = set()
                for k in range(j + 1, n):
                    sum = nums[i] + nums[j] + nums[k]
                    fourth = target - sum
                    if fourth in hash_set:
                        elements.add((nums[i], nums[j], nums[k], fourth))
                    hash_set.add(nums[k])

        return [list(quad) for quad in elements]



        # Brute Force Approach

        # nums.sort()  # Sort first so duplicates look identical
        # n = len(nums)
        # elements = set()  # Use a set to remember unique answers
        
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             for l in range(k + 1, n):
        #                 total = nums[i] + nums[j] + nums[k] + nums[l]
                        
        #                 if total == target:
        #                     # Add as a tuple (lists cannot go inside sets)
        #                     elements.add((nums[i], nums[j], nums[k], nums[l]))
        
        # # Convert the set of tuples back to a list of lists!
        # return [list(quad) for quad in elements]