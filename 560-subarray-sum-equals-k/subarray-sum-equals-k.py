class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        store = {0: 1}
        preSum, cnt = 0, 0

        for num in nums:
            preSum += num
            remove = preSum - k

            cnt += store.get(remove, 0)

            store[preSum] = store.get(preSum, 0) + 1

        return cnt