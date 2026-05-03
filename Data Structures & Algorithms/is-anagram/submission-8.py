class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        count = {}
        count2 = {}

        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count2[t[i]] = count2.get(t[i], 0) + 1
        
        return count == count2
