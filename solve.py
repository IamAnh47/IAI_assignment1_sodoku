from board import *

class Solver:
    def __init__(self, board: Board):
        self.board = board
    
    #DFS
    def solve_dfs(self,drawFlag = False):
        empty_cell = self.board.find_empty_cell()
        if not empty_cell:
            self.board.draw_grid()
            return True # Đã điền hết bảng
    
        row,col = empty_cell
        for num in range(1, 10):  # Thử các số từ 1 đến 9
            if self.board.is_valid_cell(row, col, num):
                if drawFlag:
                    self.board.update_cell_draw(row,col,num)
                else:
                    self.board.grid[row][col].set_value(num)

                if self.solve_dfs(drawFlag):  # Đệ quy
                    return True

                    #Quay Lui
                if drawFlag:
                    self.board.update_cell_draw(row,col,0)
                else:
                    self.board.grid[row][col].set_value(0)

        return False  # Không tìm được số hợp lệ
