class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            temp = n
            prod = 1

            while temp > 0:
                digit = temp % 10
                prod *= digit
                temp //= 10 
            
            if prod % t == 0:
                return n
            
            n += 1