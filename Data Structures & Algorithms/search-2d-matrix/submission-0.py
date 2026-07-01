class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if target == matrix[middle][-1] or target == matrix[middle][0]:
                return True
            elif target > matrix[middle][-1]:
                left = middle + 1
            else:
                if target > matrix[middle][0] or left == right:
                    bot = 0
                    top = len(matrix[middle]) - 1
                    while bot <= top:
                        midIndex = bot + (top - bot) // 2
                        if target == matrix[middle][midIndex]:
                            return True
                        elif target > matrix[middle][midIndex]:
                            bot = midIndex + 1
                        else:
                            top = midIndex - 1
                    return False
                else:
                    right = middle - 1
        return False
