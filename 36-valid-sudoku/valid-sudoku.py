from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowSet = defaultdict(list)
        columnSet = defaultdict(list)
        squareSet = defaultdict(list)
        for row in range(len(board)):
            for col in range(len(board[0])):
                value = board[row][col]
                if value == '.':
                    continue
                if value in rowSet.get(row,[]):
                    return False
                if value in columnSet.get(col, []):
                    return False
                if value in squareSet.get((row//3, col//3),[]):
                    return False
                rowSet[row].append(value)
                columnSet[col].append(value)
                squareSet[(row//3,col//3)].append(value)
        return True
            
                
                