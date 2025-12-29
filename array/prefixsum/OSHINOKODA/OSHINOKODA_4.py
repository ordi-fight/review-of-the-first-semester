T = int(input())                                            # No exceed memory limit of oj but exceed the limit of tume                                                            # using the for not while and don't use try and except
N = int(input())

matrix = []
for i  in range(N):                                                  # input information
    matrix.append(list(map(int,input().split())))
    
for i in range(T):
    X,Y = map(int,input().split())
                                                               #(1)
    row_center = sum(matrix[X])

    column_center = 0
    for n in range(N):                               #(2)
        if  n!= X :
            column_center += matrix[n][Y]
    
    slash_center_plus = 0
    for i in range(-N,N):                                       # matrix[X+i][Y+i], for all -N<=i<N if 0<=(X+i)<N and 0<=(Y+i)<N                 
        if 0 <=  X+i < N and 0<=(Y+i)<N and i != 0:
            slash_center_plus += matrix[X+i][Y+i] 

    slash_center_minus = 0
    for k  in  range(-N,N):                                       # matrix[X+i][Y-i], for all -N<=i<N if 0<=(X+i)<N and 0<=(Y-i)<N
        if 0<=(X+k)<N and 0<=(Y-k)<N and k != 0:             
            slash_center_minus += matrix[X+k][Y-k]
            
    print(row_center + column_center + slash_center_plus + slash_center_minus,end = "\n")