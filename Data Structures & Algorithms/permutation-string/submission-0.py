class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        count = {}
        count2 = {}

        for c in s1:
            count[c] = 1 + count.get(c, 0)

        for r in range(len(s2)):
            count2[s2[r]] = count2.get(s2[r], 0) + 1

            if (r - l + 1) > len(s1):
                count2[s2[l]] -= 1
                if count2[s2[l]] == 0:
                    del count2[s2[l]]
                l += 1
            
            if r - l + 1 == len(s1) and count2 == count:
                return True     

        return False


