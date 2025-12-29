T = int(input())                                            # exceed memory limit of oj 
N = int(input())
matrix = []
while True:                                                  # input information
    try:
        matrix.append(list(map(int,input().split())))
    except EOFError:
        break
for inds in matrix[N:] :
    X = inds[0]                                               #(1)
    Y = inds[1]
    row_center = sum(matrix[X])

    column_center = []       
    for n in range(len(matrix)):                               #(2)
        if  n < N and n!= X :
            column_center.append(matrix[n][Y])
    column_center = sum(column_center)
    slash_center_plus = []
    for i in range(-N,N):                                       # matrix[X+i][Y+i], for all -N<=i<N if 0<=(X+i)<N and 0<=(Y+i)<N                 
        if 0 <=  X+i < N and 0<=(Y+i)<N and i != 0:
            slash_center_plus.append(matrix[X+i][Y+i])
    slash_center_plus = sum(slash_center_plus)

    slash_center_minus = [] 
    for i  in  range(-N,N):                                       # matrix[X+i][Y-i], for all -N<=i<N if 0<=(X+i)<N and 0<=(Y-i)<N
        if 0<=(X+i)<N and 0<=(Y-i)<N and i != 0:
            slash_center_minus.append(matrix[X+i][Y-i])
    slash_center_minus = sum(slash_center_minus)
    print(row_center + column_center + slash_center_plus + slash_center_minus,end = "\n")