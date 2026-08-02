class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_map = {}
        square_map = {}
        for i in range(9):
            col_map[i] = set()
            for j in range(9):
                square_map[(i, j)] = set()
        for row in range(9):
            row_set = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in row_set or board[row][col] in col_map[col] or board[row][col] in square_map[row // 3, col // 3]:
                    return False
                else:
                    row_set.add(board[row][col])
                    col_map[col].add(board[row][col])
                    square_map[row // 3, col // 3].add(board[row][col])
        return True
            
                
            
                