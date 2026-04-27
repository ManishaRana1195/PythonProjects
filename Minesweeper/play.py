from minesweeper import Minesweeper 

if __name__ == "__main__":
    minesweeper = Minesweeper(10, 10, 10)
    minesweeper.print_board()

    while not minesweeper.is_completed :
        pair = input("Enter the cell like row,col: ").split(",")
        x,y = int(pair[0]), int(pair[1])
        if x < 0 or x >= 10 or y < 0 or y >= 10:
            print("Invalid cell. Try again")
            continue
        minesweeper.play(x,y)
        minesweeper.print_board()
