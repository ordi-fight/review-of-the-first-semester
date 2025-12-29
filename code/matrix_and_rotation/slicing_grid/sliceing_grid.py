def solve(n, d, matrix):
    
    ans = ""

    for f in range(2*n):
        for i in range(n):
            for j in range(n):
                if i + j == f and (f - d)**2 % 2 == 0  :
                    ans += matrix[i][j]               #  </
                if i +j == f and (f - d)**2 % 2 != 0 :           
                    ans += matrix[j][i]               #  >/

    return ans

n,d = map(int,input().split())

matrix = []
for i in range(n) :
    matrix.append(input().split())


print(solve(n, d, matrix))

