class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_left = 0
        row_right = len(matrix) - 1
        row = 0

        while row_left <= row_right:
            mid_row = (row_right + row_left) // 2

            if matrix[mid_row][0] <= target and matrix[mid_row][-1] >= target:
                row = mid_row
                break
            elif matrix[mid_row][0] > target:
                row_right = mid_row - 1
            else:
                row_left = mid_row + 1
        

        col_left = 0
        col_right = len(matrix[row]) - 1

        while col_left <= col_right:
            mid_col = (col_left + col_right) // 2
            
            if matrix[row][mid_col] == target:
                return True
            elif matrix[row][mid_col] > target:
                col_right = mid_col - 1
            else:
                col_left = mid_col + 1

        return False

        