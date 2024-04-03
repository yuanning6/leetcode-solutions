class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair: [index, height]
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            # can not extend further to the right
            while stack and h < stack[-1][1]:
                stackI, stackH = stack.pop()
                maxArea = max(maxArea, stackH * (i - stackI))
                # can extend to the left til stackI
                start = stackI
            stack.append([start, h])
        
        # the remaining heights in stack can extend to the end
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea

