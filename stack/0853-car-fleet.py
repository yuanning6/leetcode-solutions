class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [[p, s] for p, s in zip(position, speed)]

        # sort by position in descending order and go reversely because the car with the largest position's speed might change
        for p, s in sorted(pairs)[::-1]:
            stack.append((target - p) / s) # decimal
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)