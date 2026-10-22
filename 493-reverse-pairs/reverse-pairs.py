class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        return self._merge_sort(nums, 0, len(nums) - 1)

    def _merge_sort(self, nums: list[int], low: int, high: int) -> int:
        if low >= high:
            return 0
        
        mid = (low + high) // 2
        
        # Step 1: Divide and solve left & right halves recursively
        count = self._merge_sort(nums, low, mid) + self._merge_sort(nums, mid + 1, high)
        
        # Step 2: Count valid reverse pairs across the mid-point split
        count += self._count_pairs(nums, low, mid, high)
        
        # Step 3: Combine both halves into a single sorted range
        self._merge(nums, low, mid, high)
        
        return count

    def _count_pairs(self, nums: list[int], low: int, mid: int, high: int) -> int:
        """Counts valid pairs (nums[i] > 2 * nums[j]) between left and right halves."""
        count = 0
        j = mid + 1
        
        for i in range(low, mid + 1):
            while j <= high and nums[i] > 2 * nums[j]:
                j += 1
            count += (j - (mid + 1))
            
        return count

    def _merge(self, nums: list[int], low: int, mid: int, high: int) -> None:
        """Standard merge step to combine sorted subarrays nums[low..mid] and nums[mid+1..high]."""
        left = nums[low : mid + 1]
        right = nums[mid + 1 : high + 1]
        
        p1 = p2 = 0
        k = low

        while p1 < len(left) and p2 < len(right):
            if left[p1] <= right[p2]:
                nums[k] = left[p1]
                p1 += 1
            else:
                nums[k] = right[p2]
                p2 += 1
            k += 1

        while p1 < len(left):
            nums[k] = left[p1]
            p1 += 1
            k += 1

        while p2 < len(right):
            nums[k] = right[p2]
            p2 += 1
            k += 1


        # Brute Force 

        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] > 2 * nums[j]:
        #             count += 1
        # return count