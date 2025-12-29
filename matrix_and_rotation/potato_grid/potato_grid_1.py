n,d,t = map(int,input().split())
grid = []
for m in range(n):
    grid.append(input().split())

shifting = [(-1,0),(0,-1),(1,0),(0,1)]
direction = [(1,-1),(1,1),(-1,1),(-1,-1)]

i = (n-1)//2
j = (n-1)//2
center = grid[i][j]

output = center  
print(i,j)
stop = 0
for b in range(n-1):
    if 0 <= i < n and 0 <= j < n:
        s,r =shifting[d]
        i += s
        j += r
        print(i,j)
        output += grid[i][j]
    for x,y in direction:
        for a in range(n):
            if stop != 1:
                i += x
                j += y
                print(i,j)
                if 0 <= i < n and 0 <= j < n :#and not(i<(n-1)//2 and j == (n-1)//2)           
                    output += grid[i][j]
            else:
                stop = 0
                break
            if i == (n-1)//2 or j == (n-1)//2:
                stop = 1
print(output)