class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:
            code = self.encode(s)
            if code not in group:
                group[code] = []
            group[code].append(s)
        
        res = []
        for g in group.values():
            res.append(g)
        
        return res
    
    def encode(self, s: str):
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1
        
        return str(count)