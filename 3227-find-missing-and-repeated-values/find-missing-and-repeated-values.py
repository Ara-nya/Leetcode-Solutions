class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s = len(grid)
        total_number = s*s
        arr = {}
        for row in grid:
            for num in row:
                arr[num] = arr.get(num, 0) + 1
        
        repeating = 0
        missing = 0
        
        for num in range(1, total_number + 1):
            if num in arr:
                if arr[num] == 2:
                    repeating = num
            else:
                missing = num

        return [repeating, missing]
