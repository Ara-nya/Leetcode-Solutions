class Solution:
    def swapIfGreater(arr1, arr2, left, right):
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr1[right], arr2[left]

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[m:] = nums2
        # nums1.sort()

        # 1. Set up the three pointers
        p1 = m - 1          # Finger on the last real number in nums1
        p2 = n - 1          # Finger on the last number in nums2
        p_write = m + n - 1 # Finger on the very last empty zero at the back of nums1
        
        # 2. While there are still numbers in nums2 to move...
        while p2 >= 0:
            
            # If nums1 still has numbers AND the nums1 number is bigger...
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p_write] = nums1[p1] # Drop it in the empty space at the back
                p1 -= 1                    # Move the nums1 finger left
                
            # Otherwise, the nums2 number is bigger (or equal)
            else:
                nums1[p_write] = nums2[p2] # Drop it in the empty space
                p2 -= 1                    # Move the nums2 finger left
                
            # No matter what we dropped, move the empty space pointer left!
            p_write -= 1