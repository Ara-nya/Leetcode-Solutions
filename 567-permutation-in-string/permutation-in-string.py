class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windSize = len(s1)
        if windSize > len(s2):
            return False

        freq = [0] * 26
        windFreq = [0] * 26

        # Step 1: Build frequency counts for s1 and the first window of s2
        for i in range(windSize):
            freq[ord(s1[i]) - ord('a')] += 1
            windFreq[ord(s2[i]) - ord('a')] += 1

        if freq == windFreq:
            return True

        # Step 2: Slide the window across the rest of s2 one character at a time
        for i in range(windSize, len(s2)):
            # Add incoming character from the right
            windFreq[ord(s2[i]) - ord('a')] += 1
            # Remove outgoing character from the left
            windFreq[ord(s2[i - windSize]) - ord('a')] -= 1

            if freq == windFreq:
                return True

        return False
        
        
        
        
        # freq = [0] * 26

        # for i in range(len(s1)):
        #     freq[ord(s1[i]) - ord('a')] += 1
        
        # windSize = len(s1)

        # for i in range(len(s2) - windSize + 1):
        #     windIdx, idx = 0, i
        #     windFreq = [0] * 26

        #     while windIdx < windSize and idx < len(s2):
        #         windFreq[ord(s2[idx]) - ord('a')] += 1
        #         windIdx += 1
        #         idx += 1
            
        #     if freq == windFreq:
        #         return True
        
        # return False
        
        
        # perm_tuples = itertools.permutations(s1)
        # permutations = [''.join(p) for p in perm_tuples]
        # for items in permutations:
        #     if items in s2:
        #         return True
        
        # return False