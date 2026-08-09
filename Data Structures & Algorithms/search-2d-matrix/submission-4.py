class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for row in matrix:
            if target > row[-1]:
                continue
            elif target < row[0]:
                return False
            elif target == row[0] or target == row[-1]:
                return True
            else:
                left = 0
                right = len(row) - 1
                middle = (left + right) // 2
                while left <= middle and right >= middle:
                    if target == row[middle]:
                        return True
                    elif target < row[middle]:
                        right = middle - 1
                    elif target > row[middle]:
                        left = middle + 1
                    middle = (left + right) // 2
        return False