import random


class Sudoku:

    def __init__(self):
        self.size = 9
        self.row_sets = [set() for _ in range(self.size)]
        self.col_sets = [set() for _ in range(self.size)]
        self.box_sets = [set() for _ in range(self.size)]
        self.board = [[" " for _ in range(self.size)] for _ in range(self.size)]
        pass

    def generate(self):
        # fill board with atmost 20 values
        count = 20
        while count > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            value = random.randint(1, 9)
            if self.board[row][col] == " ":
                box = 3 * (row // 3) + col // 3
                if self.invalid_placement(row, col, box, value):
                    continue

                self.board[row][col] = value
                self.row_sets[row].add(value)
                self.col_sets[col].add(value)
                self.box_sets[box].add(value)
                count -= 1
            else:
                continue

    def print_board(self):
        print("-" * 31)
        for i in range(self.size):
            for j in range(self.size):
                if j == 0:
                    print(f"| {self.board[i][j]} ", end="")
                elif (j + 1) % 3 == 0:
                    print(f" {self.board[i][j]} |", end="")
                else:
                    print(f" {self.board[i][j]} ", end="")
            print("")
            if (i + 1) % 3 == 0:
                print("-" * 31)

    def invalid_placement(self, row, col, box, value):
        if (
            value in self.row_sets[row]
            or value in self.col_sets[col]
            or value in self.box_sets[box]
        ):
            return True
        return False

    def solve(self, row, col):
        if col >= self.size:
            row += 1
            col = 0

        if row >= self.size:
            return True

        # if cell is already filled
        if self.board[row][col] != " ": 
            return self.solve(row, col + 1)

        prev_value = self.board[row][col]
        for value in range(1, 10):
            box = 3 * (row // 3) + col // 3
            if self.invalid_placement(row, col, box, value):
                continue
            self.board[row][col] = value
            self.row_sets[row].add(value)
            self.col_sets[col].add(value)
            self.box_sets[box].add(value)
            if self.solve(row, col + 1):
                return True
            
            self.board[row][col] = prev_value
            self.row_sets[row].remove(value)
            self.col_sets[col].remove(value)
            self.box_sets[box].remove(value)
                    
        return False


if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.generate()
    sudoku.print_board()
    print("Sudoku Solution")
    sudoku.solve(0, 0)
    sudoku.print_board()
