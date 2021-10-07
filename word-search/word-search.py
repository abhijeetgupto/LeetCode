class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(mat, word, r, c, memo):
            if not word:
                return True
    
            else:
                traverse = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                for l in traverse:
                    row, col = l
                    if 0 <= row < len(mat) and 0 <= col < len(mat[0]):
                        if mat[row][col] == word[0] and f"{row},{col}" not in memo:
                            memo.add(f"{row},{col}")
                            if helper(mat, word[1:], row, col, memo):
                                return True
                            else:
                                memo.remove(f"{row},{col}")
                return False
    
        word = list(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    x = helper(board, word[1:], i, j, {f"{i},{j}"})
                    if x:
                        return True
        print(board)
        return False