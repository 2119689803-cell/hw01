from typing import List

class NQueensSolver:
    def __init__(self, n: int):
        self.n = n
        self.solutions = []
        
        # 优化：使用集合记录已被占用的列和对角线 (空间换时间)
        self.cols = set()
        self.diag1 = set() # 主对角线 (row - col)
        self.diag2 = set() # 副对角线 (row + col)

    def solve(self) -> List[List[str]]:
        self._backtrack([], 0)
        return self.solutions

    def _backtrack(self, board: List[int], row: int):
        # 找到一个合法解
        if row == self.n:
            self.solutions.append(self._format_board(board))
            return
            
        for col in range(self.n):
            # O(1) 复杂度检查冲突
            if col in self.cols or (row - col) in self.diag1 or (row + col) in self.diag2:
                continue
                
            # 做选择
            board.append(col)
            self.cols.add(col)
            self.diag1.add(row - col)
            self.diag2.add(row + col)
            
            # 递归进入下一行
            self._backtrack(board, row + 1)
            
            # 撤销选择 (回溯)
            board.pop()
            self.cols.remove(col)
            self.diag1.remove(row - col)
            self.diag2.remove(row + col)

    def _format_board(self, board: List[int]) -> List[str]:
        # 将一维数组 [1, 3, 0, 2] 转换为棋盘字符串形式
        return ["." * c + "Q" + "." * (self.n - c - 1) for c in board]
