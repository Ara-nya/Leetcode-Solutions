class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "", 1) #The 1 specifies only removes the leftmost occurrence in each loop step

        return s