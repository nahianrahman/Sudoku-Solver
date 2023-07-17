from tkinter import *


root = Tk()
root.geometry('275x320')


# Solve the Sudoku
class SolveSudoku():
    def __init__(self):
        self.set_zero()
        self.solve()


    # Set the empty cells to 0
    def set_zero(self):
        for row in range(9):
            for col in range(9):
                if entered_numbers[row][col].get() not in ['1','2','3','4','5','6','7','8','9']:
                    entered_numbers[row][col].set(0)


    def solve(self):
        row, col = self.find_empty_square()
        
        # no square left so all inputs correct and solved
        if row is None:
            return True

        # try guesses from 1 to 9
        for guess in range(1, 10):
            if self.is_valid(guess, row, col):
                entered_numbers[row][col].set(guess)
                if self.solve():
                    return True

                # reset to 0 if not correct
                entered_numbers[row][col].set(0)

        # none of the numbers work, so unsolvable
        return False 

    def find_empty_square(self):
        for row in range(9):
            for col in range(9):
                if entered_numbers[row][col].get() == '0':
                    return row, col

        return None, None

  
    def is_valid(self, guess, row, col):
        # Check Row
        for j in range(9):
            if entered_numbers[row][j].get() == str(guess):
                return False

        # Check Column
        for i in range(9):
            if entered_numbers[i][col].get() == str(guess):
                return False
            
        # Check Box
        # Find the first cell coordinates of the block containing the selected cell    
        row_start, col_start = 3 * (row//3), 3 * (col//3)
        for i in range(row_start, row_start+3):
            for j in range(col_start, col_start+3):
                if entered_numbers[i][j].get() == str(guess):
                    return False
        
        return True


class Launch():  
    def __init__(self, root):
        
        # Title and settings
        self.root = root
        root.title("Sudoku Solver")

        font = ('Arial', 18)
        color = 'white'
        px, py = 0, 0

        # Design the Grid
        self.__table = []
        for i in range(9):
            self.__table += [[0,0,0,0,0,0,0,0,0]]

        for i in range(9):
            for j in range(9):
                
                if (i < 3 or i > 5) and (j < 3 or j > 5):
                    color = '#FDD128'
                elif i in [3,4,5] and j in [3,4,5]:
                    color = '#FDD128'
                else:
                    color = '#F8E472'

                self.__table[i][j] = Entry(root, width = 2, font = font, bg = color, cursor = 'arrow', borderwidth = 0,
                                          highlightcolor = 'white', highlightthickness = 1, highlightbackground = 'black',
                                          textvar = entered_numbers[i][j])
                self.__table[i][j].bind('<Motion>', self.reset_cell)
                self.__table[i][j].bind('<FocusIn>', self.reset_cell)
                self.__table[i][j].bind('<Button-1>', self.reset_cell)
                self.__table[i][j].grid(row=i, column=j)


        # Buttons
        solve_button = Button(root, text='Solve', width=7, bg='green', font='Arial', command=self.solve_input)
        clear_button = Button(root, text = 'Clear All', width=7, font='Arial', command=self.clear)
        exit_button = Button(root, text='Exit', width=7, bg='red', font='Arial', command=root.quit)

        solve_button.grid(row=9, column=0, columnspan=3, pady=5)
        clear_button.grid(row=9, column=3, columnspan=3, pady=5)
        exit_button.grid(row=9, column=6, columnspan=3, pady=5)
        

    # Reset the Cell if inputs are invalid
    def reset_cell(self, event):
        for row in range(9):
            for col in range(9):
                if entered_numbers[row][col].get() == '':
                    continue
                if len(entered_numbers[row][col].get()) > 1 or entered_numbers[row][col].get() not in ['1','2','3','4','5','6','7','8','9']:
                    entered_numbers[row][col].set('')


    # Clear the Grid
    def clear(self):
        for row in range(9):
            for col in range(9):
                entered_numbers[row][col].set('')


    # Calls SolveSudoku
    def solve_input(self):
        solution = SolveSudoku()
        

# Global Matrix to store the numbers
entered_numbers = []
for i in range(9):
    entered_numbers += [[0,0,0,0,0,0,0,0,0]]
for row in range(9):
    for col in range(9):
        entered_numbers[row][col] = StringVar(root)


app = Launch(root)
root.mainloop()
