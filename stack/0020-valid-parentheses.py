class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = { ")":"(", "}":"{", "]":"[" }

        for c in s:
            # if it's closing character
            if c in map:
                if stack and stack[-1] == map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
            