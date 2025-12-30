def bright(N_matrix:list,N:int) -> int :              #fill in the valuable we need

    row = [0]*N
    col = [0]*N
    right = [0]*(2*N)
    left = [0]*(2*N)

    for i in range(N):                                # n*2 times and sum doesn't time one time
        for j in range(N):
            a = N_matrix[i][j]                        # define a and assign value:N_matrix[i][j] to a
            row[i] += a                               #infromations with the same i save in the same box in the 1 dimension array to take in the form of summation
            col[j]  += a                              #infromations with the same j save in the same box in the 1 dimension array to take in the form of summation
            left[i-j+N-1] += a                        #infromations with the same i-j+N-1 save in the same box in the 1 dimension array to take in the form of summation
            right[i+j] += a                           #infromations with the same i+j save in the same box in the 1 dimension array to take in the form of summation
            
    return row,col,right,left                         # def difinately need a return if you want to use the value                        


T = int(input())                                       #input
N = int(input())

N_matrix = []
for m in range(N):                                     # use for loop to minimize the memory consumption  

    N_matrix.append(list(map(int,input().split())))    # input 1 dimension array

row, col, right, left = bright(N_matrix, N)                         #the prefix sum executes once is enough , if you put it in the loop,you execute T times. And the prefix sum executes n**2 times  
for n in range(T):

    x,y = map(int,input().split())

                                                                    # row 、 col 、 left 、right can only be used after you call bright function
                                                                    # call bright function and assign it to 
    print(row[x]+col[y]+left[x-y+N-1]+right[x+y]-N_matrix[x][y]*3)


#time limit exceeds