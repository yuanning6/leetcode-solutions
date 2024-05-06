# Heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # O(nlogk)
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]

# Quick select
# O(n) on best and average, O(n^2) in the worst case