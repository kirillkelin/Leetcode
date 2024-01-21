class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dct_row = {key: set() for key in range(9)}
        dct_col = {key: set() for key in range(9)}
        dct_boxes = {(i, j): set() for i in range(3) for j in range(3)}

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue

                box_key = (row // 3, col // 3)
                if board[row][col] in dct_row[row] or board[row][col] in dct_col[col] or board[row][col] in dct_boxes[
                    box_key]:
                    return False

                dct_row[row].add(board[row][col])
                dct_col[col].add(board[row][col])
                dct_boxes[box_key].add(board[row][col])

        return True