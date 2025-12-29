T = int(input())                                            # exceed memory limit of oj 
N = int(input())
matrix = []
while True:                                                  # input information
    try:
        matrix.append(list(map(int,input().split())))
    except EOFError:
        break
print(matrix[0][0])


# the conclusion the try and except need very much time and memory