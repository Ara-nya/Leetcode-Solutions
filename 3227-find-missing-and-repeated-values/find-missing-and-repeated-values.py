class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        total_elements = N * N
        
        SN = (total_elements * (total_elements + 1)) // 2
        SN2 = (total_elements * (total_elements + 1) * (2 * total_elements + 1)) // 6
        
        S = 0
        S2 = 0
        
        for row in grid:
            for val in row:
                S += val
                S2 += val * val

        val1 = S - SN
        val2 = S2 - SN2
        val2 = val2 // val1

        x = (val1 + val2) // 2
        y = x - val1
        
        return [x, y]


        # xr = 0
        
        # for row in grid:
        #     for val in row:
        #         xr = xr ^ val

        # for num in range(1, total_elements + 1):
        #     xr = xr ^ num

        # bitNo = xr & ~(xr - 1)
        
        # zero = 0
        # one = 0
        
        # for row in grid:
        #     for val in row:
        #         if val & bitNo:
        #             one = one ^ val
        #         else:
        #             zero = zero ^ val
                    
        # for num in range(1, total_elements + 1):
        #     if num & bitNo:
        #         one = one ^ num
        #     else:
        #         zero = zero ^ num

        # for row in grid:
        #     for val in row:
        #         if val == zero:
        #             return [zero, one]
                    
        # return [one, zero]