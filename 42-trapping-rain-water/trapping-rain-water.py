class Solution:
    def trap(self, height: List[int]) -> int:
        lMax, rMax, total, l, r = 0, 0, 0, 0, len(height) - 1
        while l < r:
            if height[l] <= height[r]:
                if lMax > height[l]:
                    total += lMax - height[l]
                else:
                    lMax = height[l]
                l = l + 1
            else:
                if rMax > height[r]:
                    total += rMax - height[r]
                else:
                    rMax = height[r]
                r = r - 1
        return total