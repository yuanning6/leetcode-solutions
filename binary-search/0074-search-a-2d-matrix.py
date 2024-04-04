class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bott = 0, ROWS - 1
        while top <= bott:
            row = top + ((bott - top) // 2)
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bott = row - 1
            else:
                break
        
        if top > bott:
            return False
        
        l, r = 0, COLS - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return False