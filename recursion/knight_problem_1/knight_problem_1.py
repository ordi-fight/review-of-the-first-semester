T = int(input())
for f in range(T):
    m,n = map(int,input().split())

    moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    board = []
    for v in range(m):
        board.append(list(map(int,input().split())))

    def dfs(i,j,step):

        if step == m*n -1:
            return True
        for dx,dy in moves:
            x,y = i+dx,j+dy
            if  0 <= x < m and 0 <= y < n and board[x][y] == step+1:
                if dfs(x,y,step+1):
                    return True
        return False

    if not dfs(0,0,0):
        print("Dirty Work")

    if dfs(0,0,0):
        print("How sweet")