class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0] * 26

        for i in range(len(s1)):
            freq[ord(s1[i]) - ord('a')] += 1
        
        windSize = len(s1)

        for i in range(len(s2) - windSize + 1):
            windIdx, idx = 0, i
            windFreq = [0] * 26

            while windIdx < windSize and idx < len(s2):
                windFreq[ord(s2[idx]) - ord('a')] += 1
                windIdx += 1
                idx += 1
            
            if freq == windFreq:
                return True
        

        return False
        
        
        # perm_tuples = itertools.permutations(s1)
        # permutations = [''.join(p) for p in perm_tuples]
        # for items in permutations:
        #     if items in s2:
        #         return True
        
        # return False