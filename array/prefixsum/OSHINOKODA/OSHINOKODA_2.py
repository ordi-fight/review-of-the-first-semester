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
    sum_center = sum(matrix[X])

         
    for n in range(len(matrix)):                               #(2)
        if  n < N and n!= X :
            sum_center += sum([matrix[n][Y]])
    
    
    for i in range(-N,N):                                       # matrix[X+i][Y+i], for all -N<=i<N if 0<=(X+i)<N and 0<=(Y+i)<N                 
        if 0 <=  X+i < N and 0<=(Y+i)<N and i != 0:
            sum_center+= sum([matrix[X+i][Y+i]])
    

    for i  in  range(-N,N):                                       # matrix[X+i][Y-i], for all -N<=i<N if 0<=(X+i)<N and 0<=(Y-i)<N
        if 0<=(X+i)<N and 0<=(Y-i)<N and i != 0:
            sum_center += sum([matrix[X+i][Y-i]])

    print(sum_center,end = "\n")