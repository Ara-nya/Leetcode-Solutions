class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
            
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
            
        return answer

        



        # Brute Force
        
        # answer = []
        # for i in range(len(nums)):
        #     mul = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         else:
        #             mul *= nums[j]
        #     answer.append(mul)

        # return answer