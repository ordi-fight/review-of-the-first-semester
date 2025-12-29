for b in range(1,n):
    i = i - 1                                      #change with d
    if  (0 <= i < n) and 0 <= j < n:
        start = grid[i][j] 
    else:
        start = ""

    for a in range(1,b+1):                          #left_up
        if (0 <= i+a < n) and (0 <= j-a < n):
            output += grid[i+a][j-a]
        else:
            output += ""
        i += 1
        j -= 1
    for a in range(1,b+1)                           #left_down
        if  i+a < n and  j+a < n:
            output += grid[i+a][j+a]
        else:
            output += ""
        i += 1
        j += 1

    for a in range(1,b+1):                           #right_up
        if 0 <= i-a and 0 <= j-a:
            output += grid[i-a][j-a]
        else:
            output += ""
        i -= 1
        j -= 1
    for a in range(1,b+1):                          #right_down
        if 0 <= i-a and j+a < n:
            output += grid[i-a][j+a]
        else:
            output += ""
        
        i -= 1
        j += 1
def start(i,j,grid):
    if  (0 <= i < n) and 0 <= j < n:
        start = grid[i][j] 
    else:
        start = ""

def left_up(b,output,i,j,grid):
    for a in range(1,b+1):                          #left_up
        if (0 <= i+a < n) and (0 <= j-a < n):
            output += grid[i+a][j-a]
        else:
            output += ""
        i += 1
        j -= 1
def left_down(b,output,i,j,grid):
    for a in range(1,b+1)                           #left_down
        if  i+a < n and  j+a < n:
            output += grid[i+a][j+a]
        else:
            output += ""
        i += 1
        j += 1
    
def right_up(b,output,i,j,grid)
    for a in range(1,b+1):                           #right_up
        if 0 <= i-a and 0 <= j-a:
            output += grid[i-a][j-a]
        else:
            output += ""
        i -= 1
        j -= 1
def right_down(b,output,i,j,grid):
    for a in range(1,b+1):                          #right_down
        if 0 <= i-a and j+a < n:
            output += grid[i-a][j+a]
        else:
            output += ""
        i -= 1
        j += 1