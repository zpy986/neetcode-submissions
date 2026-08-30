class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(i):
            hashmap = {}
            for j in range(len(board[0])):
                if board[i][j] != "." and board[i][j] in hashmap:
                    return False
                hashmap[board[i][j]] = 1
            
            return True
        
        def checkCol(j):
            hashmap = {}
            for i in range(len(board)):
                if board[i][j] != "." and board[i][j] in hashmap:
                    return False
                hashmap[board[i][j]] = 1
            
            return True

        def checkSubBox(i, j):
            hashmap = {}
            for ni in range(3):
                for nj in range(3):
                    if board[i + ni][j + nj] != "." and board[i + ni][j + nj] in hashmap:
                        return False
                    hashmap[board[i + ni][j + nj]] = 1
            
            return True
        
        for i in range(len(board)):
            if checkRow(i) == False:
                return False
        for j in range(len(board[0])):
            if checkCol(j) == False:
                return False
        for i in range(len(board) // 3):
            for j in range(len(board) // 3):
                if checkSubBox(i * 3, j * 3) == False:
                    return False

        return True

            