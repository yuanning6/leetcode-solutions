# mock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        res = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                res = max(res, prices[r] - prices[l])
            else:
                l = r
            
            r = r + 1

        return res