def start(n,i,j,grid):
    if  (0 <= i < n) and 0 <= j < n:                
        start_point= grid[i][j] 
    else:
        start_point = ""
    return start_point
def left_up(n,b,i,j,grid):
    left_up_sum = "" 
    for a in range(1,b+1):                          #left_up
        if (0 <= i+a < n) and (0 <= j-a < n):
            left_up_sum += grid[i+a][j-a]
        else:
            left_up_sum += ""
        
    return left_up_sum
def left_down(n,b,i,j,grid):
    left_down_sum = ""
    for a in range(1,b+1):                           #left_down
        if  i+a < n and  j+a < n:
            left_down_sum += grid[i+a][j+a]
        else:
            left_down_sum += ""
        
    return left_down_sum
def right_up(n,b,i,j,grid):
    right_up_sum = ""
    for a in range(1,b+1):                           #right_up
        if 0 <= i-a and 0 <= j-a:
            right_up_sum += grid[i-a][j-a]
        else:
            right_up_sum += ""
        
    return right_up_sum
def right_down(n,b,i,j,grid):
    right_down_sum = ""
    for a in range(1,b+1):                          #right_down
        if 0 <= i-a and j+a < n:
            right_down_sum += grid[i-a][j+a]
        else:
            right_down_sum += ""
        
    return right_down_sum
def solve(n,d,t,grid):

    ans = ""

    center = grid[(n+1)//2-1][(n+1)//2-1]

    i = (n+1)//2 - 1
    j = (n+1)//2 -1

    output = center

    if t == 0:
        for b in range(1,n):
            match d:
                case 0 :
                    if  i == (n+1)//2 - 1 and j == (n+1)//2 -1:
                        i = i - 1
                        output += start(n,i,j,grid) 
                    else:
                        i -= 2
                        j -= 1
                    output += left_up(n,b,i,j,grid)
                    # print(f"left_up(n,b,i,j,grid) 's i, j is {i},{j} ") 
                    i += b
                    j -= b
                    output +=  left_down(n,b,i,j,grid)
                    # print(f"left_down(n,b,i,j,grid) is {left_down(n,b,i,j,grid)} and {i},{j}")
                    i += b
                    j += b
                    output += right_down(n,b,i,j,grid)
                    # print(f"right_down(n,b,i,j,grid) is {right_down(n,b,i,j,grid)} and {i},{j}")
                    i -= b
                    j += b
                    output += right_up(n,b-1,1,j,grid)
                    i -= (b-1)
                    j -= (b-1)
                case 1:
                    if i == (n+1)//2 - 1 and j == (n+1)//2 -1:
                        j = j - 1
                        output += start(n,i,j,grid)
                    else:
                        i += 1
                        j -= 2
                    output += left_down(n,b,i,j,grid)
                    i += b
                    j += b 
                    output += right_down(n,b,i,j,grid)
                    i -= b
                    j += b 
                    output += right_up(n,b,i,j,grid)
                    i -= b
                    j -= b
                    output += left_up(n,b-1,1,j,grid)
                    i += (b-1)
                    j -= (b-1)
                case 2:
                    if i == (n+1)//2 - 1 and j == (n+1)//2 -1:
                        i = i + 1 
                        output += start(n,i,j,grid)
                    else:
                        i += 2
                        j += 1
                    output += right_down(n,b,i,j,grid)
                    i -= b
                    j += b
                    output += right_up(n,b,i,j,grid) 
                    i -= b
                    j -= b
                    output += left_up(n,b,i,j,grid)
                    i += b
                    j -= b
                    output += left_down(n,b-1,1,j,grid)
                    i += (b-1)
                    j += (b-1)
                case 3:
                    if i == (n+1)//2 - 1 and j == (n+1)//2 -1:
                        j = j + 1
                        output += start(n,i,j,grid)
                    else:
                        i -= 1
                        j += 2
                    output += right_up(n,b,i,j,grid) 
                    i -= b
                    j -= b
                    output += left_up(n,b,i,j,grid)
                    i += b
                    j -= b
                    output += left_down(n,b,i,j,grid)
                    i += b
                    j += b
                    output += right_down(n,b-1,1,j,grid)
                    i -= (b-1)
                    j += (b-1)
    if t == 1:
        for b in range(1,n):
            match d:
                case 0:
                    if  i == (n+1)//2 - 1 and j == (n+1)//2 -1:
                        i = i - 1
                        output += start(n,i,j,grid) 
                    else:
                        i -= 2
                        j += 1
                    output += left_down(n,b,i,j,grid)
                    # print(f"left_up(n,b,i,j,grid) 's i, j is {i},{j} ") 
                    i += b
                    j += b
                    output +=  left_up(n,b,i,j,grid)
                    # print(f"left_down(n,b,i,j,grid) is {left_down(n,b,i,j,grid)} and {i},{j}")
                    i += b
                    j -= b
                    output += right_up(n,b,i,j,grid)
                    # print(f"right_down(n,b,i,j,grid) is {right_down(n,b,i,j,grid)} and {i},{j}")
                    i -= b
                    j -= b
                    output += right_down(n,b-1,1,j,grid)
                    i -= (b-1)
                    j += (b-1)
                case 1:
                    if i == (n+1)//2 - 1 and j == (n+1)//2 -1:
                        j = j - 1
                        output += start(n,i,j,grid)
                    else:
                        i -= 1
                        j -= 2
                    output += right_down(n,b,i,j,grid)
                    i -= b
                    j += b 
                    output += left_down(n,b,i,j,grid)
                    i += b
                    j += b 
                    output += left_up(n,b,i,j,grid)
                    i += b
                    j -= b
                    output += right_up(n,b-1,1,j,grid)
                    i -= (b-1)
                    j -= (b-1)
                case 2:
                    if i == (n+1)//2 - 1 and j == (n+1)//2 -1:
                        i = i + 1 
                        output += start(n,i,j,grid)
                    else:
                        i += 2
                        j -= 1
                    output += right_up(n,b,i,j,grid)
                    i -= b
                    j -= b
                    output += right_down(n,b,i,j,grid) 
                    i -= b
                    j += b
                    output += left_down(n,b,i,j,grid)
                    i += b
                    j += b
                    output += left_up(n,b-1,1,j,grid)
                    i += (b-1)
                    j -= (b-1)
                case 3:
                    if i == (n+1)//2 - 1 and j == (n+1)//2 -1:
                        j = j + 1
                        output += start(n,i,j,grid)
                    else:
                        i += 1
                        j += 2
                    output += left_up(n,b,i,j,grid) 
                    i += b
                    j -= b
                    output += right_up(n,b,i,j,grid)
                    i -= b
                    j -= b
                    output += right_down(n,b,i,j,grid)
                    i -= b
                    j += b
                    output += left_down(n,b-1,1,j,grid)
                    i += (b-1)
                    j += (b-1)
    return output

n,d,t = map(int,input().split())
grid = []
for i in range(n):

    grid.append(input().split())
# print(grid)
print(solve(n,d,t,grid))



