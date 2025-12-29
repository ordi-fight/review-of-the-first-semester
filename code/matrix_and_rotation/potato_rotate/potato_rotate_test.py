# import time
# import random
# matrix = [[random.randint(0,9) for _ in range(100)] for _ in range(100)]
# n,m,k = 100,100,100
# start = time.time()
n,m,k = map(int,input().split())
if n > m:
    width = n
if m > n:
    width = m
if n == m:
    width = m
matrix = [[None]*(width) for _ in range(width)]

for v in range(n):
    matrix[v][:m] = input().split()
for _ in range(k%4):
    temp = [[None]*width for _ in range(width)]
    for x in range(0,width):
        for y in range(0,width):
            temp[y][width-1-x] = matrix[x][y]
        
    lst = []
    for x in range(0,width):
        matrix[x] = temp[x] 
        if matrix[x] != [None]*width:
            storage = []
            for y in range(0,width):
                if matrix[x][y] != None:
                    storage.append(matrix[x][y])
            lst.append(storage)
for f in lst:
    print(" ".join(list(map(str,f))))
# end = time.time()
# print(f"執行時間：{end - start:.5f} 秒")