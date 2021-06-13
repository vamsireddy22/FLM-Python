# Read Inputing 

# Global variable - Present outside the function body and accessible to every function. 
# Local variable - Defined inside the function and able to access only inside that function 

puzzle = [
    [5,3,-1,6,7,8,9,-1,2],
    [6,7,2,1,9,5,3,4,8],
    [-1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,-1,4,8,5,6]
    [9,6,-1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]


def columnWise(i,j,choice):
    # Check columnwise and return false if we foud the choice already exist in coulumn else 
    # return true
    global puzzle
    for row in range(0,9):
        if(puzzle[row][j] == choice):
            return False
    return True


def rowWise(i,j,choice):
    # Check rowise and return false if we foud the choice already exist in row else 
    # return true
    global puzzle
    for col in range(0,9):
        if(puzzle[i][col] == choice):
            return False
    return True



def isSafePlace(i,j,choice):
    # Satisfy 3 rules 
    # 1. Rowwise check 2. Columnwise 3. BlockWise
    if(rowWise(i,j,choice) and columnWise(i,j,choice) and blockWise(i,j,choice)):
        return True
    else:
        return False


def sudokuSolver():
    global puzzle 
    # I need to fix row 
    for i in range(0,9):
        # Iterate colunwise by fixing one row
        for j in range(0,9):
            # Check for -1
            if(puzzle[i][j] == -1):
                # Check for choice for placing 
                for choice in range(1,10):
                    if(isSafePlace(i,j,choice)):
                        pass






sudokuSolver()