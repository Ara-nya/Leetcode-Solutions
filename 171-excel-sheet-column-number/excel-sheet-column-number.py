class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        sum = 0
        for i in range (len(columnTitle)):
            temp = columnTitle[len(columnTitle) - i - 1]
            sum = sum + ((ord(temp) - 64)*(26**i))
        return sum