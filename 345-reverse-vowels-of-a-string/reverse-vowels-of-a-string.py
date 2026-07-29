class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        
        left = 0
        right = len(s_list) - 1
        
        vowels = 'AEIOUaeiou' 
        
        while left < right:
            if s_list[left] in vowels and s_list[right] in vowels:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left = left + 1
                right = right - 1
            elif s_list[left] not in vowels:
                left = left + 1
            elif s_list[right] not in vowels:
                right = right - 1

        return "".join(s_list)