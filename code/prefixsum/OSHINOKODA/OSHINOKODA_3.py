
T = int(input()) 
N = int(input())                                           

N_matrix = []

for m in range(N):

    N_matrix.append(list(map(int,input().split())))

for k in range(T):
    x,y = map(int,input().split())

    left = [0]*(2*N)
    right = [0]*(2*N)

    row = sum(N_matrix[x])
    col = sum(N_matrix[i][y] for i in range(N))

    for i in range(N):
        for j in range(N):
            left[i-j+N-1] += N_matrix[i][j]                         #此儲存格多一個元素，以總和的方式儲存在一維陣列
            right[i+j] += N_matrix[i][j]
    print(row+col+left[x-y+N-1]+right[x+y]-N_matrix[x][y]*3)        #記得還要留一個，不要減過頭，減成N_matrix[x][y]*4，這樣的話星星位置會缺空
    

    

    