class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT
    
# mock
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        smap = {} # letter -> frequency
        tmap = {}

        for i in range(len(s)):
            smap[s[i]] = smap.get(s[i], 0) + 1
            tmap[t[i]] = tmap.get(t[i], 0) + 1
        
        return True if smap == tmap else False