board = [
    [0,0,0,0,4,2,5,7,6],
    [0,5,0,0,0,1,3,8,4],
    [0,0,0,0,5,0,1,9,2],
    [0,2,0,1,6,9,4,3,5],
    [0,0,0,7,3,8,2,1,9],
    [0,0,9,5,2,4,7,6,8],
    [2,0,7,0,9,0,8,4,3],
    [3,6,4,2,8,7,9,5,0],
    [0,9,5,4,0,0,6,2,7]
]

def solve(bo):
    
    find = find_empty(bo)
    if find:
        row, col = find
    else:
        return True
    
    for i in range(1, 10):
        if valid(bo, (row, col), i):
            bo[row][col] = i

            if solve(bo):
                return True
            
            bo[row][col] = 0
    
    return False

def valid(bo, pos, num):
    
    # check row
    for i in range(0, len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    
    # check column
    for i in range(0, len(bo)):
        if bo[i][pos[1]] == num and pos[1] != i:
            return False
    
    #check box
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    
    return True

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    
    return None

print_board(board)
solve(board)
print("_________")
print_board(board)