from tabulate import tabulate

# A 9x9 sudoku matrix as the input

sudoku_matrix = [
               [5, 3, 0, 0, 7, 0, 0, 0, 0],
               [6, 0, 0, 1 ,9, 5, 0, 0, 0],
               [0, 9, 8, 0, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 6, 0, 0, 0, 3],
               [4, 0, 0, 8, 0, 3, 0, 0, 1],
               [7, 0, 0, 0, 2, 0, 0, 0, 6],
               [0, 6, 0, 0, 0, 0, 2, 8, 0],
               [0, 0, 0, 4, 1, 9, 0, 0, 5],
               [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

#Display the matirx
def display(sudoku_matrix):
    print(tabulate(sudoku_matrix, tablefmt = 'fancy_grid'))

#Finding an empty cell
def emptyCell():
    for i in range(9):
        for j in range(9):
            if(sudoku_matrix[i][j] == 0):
                return[i, j]
    return False

#Checking if the value is a possible answer
def validNum(num, i, j):
    #This checks if the number is already present in the corresponding row / column / 3*3 block

    #Check if it's a valid value in the row
    for col in range(9):
        if(sudoku_matrix[i][col] == num):
            return False

    #Check if it's a valid value in the coloumn
    for row in range(9):
        if(sudoku_matrix[i][row] == num):
            return False

    #creating grid iterators
    iterRow = (i // 3) * 3
    iterCol = (j // 3) * 3

    #Checking for the value in the grid
    #iteratorRow goes through the elemnts of the row of the grid
    #itereatorCol goes through the elements of the columns of the grid
    for iteratorRow in range(iterRow, iterRow + 3):
        for iteratorCol in range(iterCol, iterCol + 3):
            if(sudoku_matrix[iteratorRow][iteratorCol] == num):
                return False

    #If all the cases are passed, then 'num' is a possible solution
    return True

def solver():
    cellsExist = emptyCell()

    #If there are no longer any empty cells.
    if(not cellsExist):
        return True

    i = cellsExist[0]
    j = cellsExist[1]

    for num in range(1,10):
        if(validNum(num, i, j)):
            sudoku_matrix[i][j] = num

            #The "Backpropogation bit"
            #If the solution is valid then we proceed and guess a value for the next empty cell
            if(solver()):
                return True
            else:
                #This means that our current guess hasn't worked. So we mark the cell as empty and try out another value
                sudoku_matrix[i][j] = 0

    #If there is none of the values worked
    return False

#Displaying the board before solving
display(sudoku_matrix)

if(solver()):
    #The solved matrix
    display(sudoku_matrix)
else:
    print("There is no possible solution :(")
