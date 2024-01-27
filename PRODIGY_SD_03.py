import tkinter as tk
import copy


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
    print("---------------------------------------------------- \n")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, col

    return None


def solve_sudoku():

    """"
    # Extract values from Entry widgets and create 2D list (Sudoku board)
    board = [[0]*9 for _ in range(9)]

    for i in range(9):
    for j in range(9):
        value = entries[i][j].get()
        board[i][j] = int(value) if value.isdigit() else 0

    """

    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    original_board = copy.deepcopy(board)

    # Update the GUI with the solved values
    for i in range(9):
        for j in range(9):
            if board[i][j] == original_board[i][j] and board[i][j] != 0:
                color = "green"
            else:
                color = "blue"

            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, str(board[i][j]))
            entries[i][j].config(fg=color)


root = tk.Tk()
root.geometry("300x450")
root.title("Sudoku Solver")

background_image = tk.PhotoImage(file="task3_image.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

title_label = tk.Label(root, text="Sudoku Solver", font=("Consolas", 12), bg="#55637A", fg='white')
title_label.grid(padx=10, pady=10, columnspan=20)

# Create a 9x9 grid of entry widgets
entries = [[tk.Entry(root, width=3) for _ in range(9)] for _ in range(9)]

# this x and y is just for spacing
x = 0
y = 0

for r in range(9):
    x = 0
    if r % 3 == 0 and r != 0:
        tk.Label(root, text="\n").grid(row=y + 5, column=x)
        y = y + 1

    for c in range(9):
        if c % 3 == 0:
            tk.Label(root, text="", font=("Consolas", 0)).grid(row=y+5, column=x)
            x = x + 1
        entries[r][c].grid(row=y+5, column=x, padx=3, pady=3)
        x = x + 1

    y = y + 1


# click this button to solve the sudoku
solve_button = tk.Button(root, text="Solve", font=("Consolas", 12), bg="#55637A", fg='white', command=solve_sudoku)
solve_button.grid(row=20, columnspan=20, padx=10, pady=10, ipadx=10, ipady=10)

root.mainloop()
