class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # freq[i] will store the numbers that appear i times
        freq = [[] for i in range(len(nums) + 1)]

        # Count the frequency of each number
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Store the numbers that appear i times
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    break
        
        return res