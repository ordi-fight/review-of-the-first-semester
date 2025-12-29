m, n = map(int,input().split())
board = []
for i in range(m):
    board.append([-1]*n)
    # 騎士移動的 8 種方向，且按照你題目給的優先順序
moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]


def dfs(i, j, step):
    board[i][j] = step
    if step == m * n - 1:
        return True

    for dx, dy in moves:
        x, y = i + dx, j + dy
        if 0 <= x < m and 0 <= y < n and board[x][y] == -1:
            if dfs(x, y, step + 1):   #(i = x and j =  y)再跑下一個遞迴 step 0 有一遞迴 step 1有......這步要往下一個遞迴
                return True    #(其實只是要讓這分支的遞迴停止而已)

    board[i][j] = -1
    return False
if dfs(0,0,0):
    print(board)