class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(reversed(words))


        # Brute Force

        # words = s.split()
        # n = len(words)

        # s = ""

        # for i in range(n - 1, -1, -1):
        #     if i == 0:
        #         s = s + words[i]
        #         break

        #     s = s + words[i] + " "

        # return s