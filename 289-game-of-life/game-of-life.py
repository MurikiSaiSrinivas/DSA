class Solution(object):
    def getCounts(self, i, j,board, r,c):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), 
                  (1, 1), (1, 0), (1, -1), (0, -1)]
        zeroCounts = 0
        oneCounts = 0
        for dr,dc in directions:
            ni = i + dr
            nj = j + dc
            if 0 <= ni and  ni < r and 0 <= nj and nj < c:
                if board[ni][nj] == 0:
                    zeroCounts += 1
                else: 
                    oneCounts += 1
        return zeroCounts, oneCounts

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        r = len(board)
        c = len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
                      (1, 1), (1, 0), (1, -1), (0, -1)]

        # Fix: create deep copy for newBoard
        newBoard = [[0] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                live_neighbors = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < r and 0 <= nj < c:
                        if board[ni][nj] == 1:
                            live_neighbors += 1

                if board[i][j] == 1:
                    if live_neighbors in [2, 3]:
                        newBoard[i][j] = 1  # survives
                else:
                    if live_neighbors == 3:
                        newBoard[i][j] = 1  # reproduction

        # Fix: copy back to original board (in-place update)
        for i in range(r):
            for j in range(c):
                board[i][j] = newBoard[i][j]
                         
