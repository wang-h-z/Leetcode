from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9): 
            for j in range(9): 
                if board[i][j] != ".":
                    char = board[i][j]
                    box_id = i // 3 * 3 + j // 3
                    if char in rows[i] or char in cols[j] or char in boxes[box_id]: 
                        return False
                    else: 
                        rows[i].add(char)
                        cols[j].add(char)
                        boxes[box_id].add(char)
        return True