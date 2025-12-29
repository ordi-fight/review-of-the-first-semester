# import random
# matrix = [[random.randint(0,9) for _ in range(100)] for _ in range(100)]
# import time
# start = time.time()
# n,m,k = 100,100,900
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
        
    for x in range(0,width):
        matrix[x] = temp[x]
for x in matrix: 
    if x != [None]*width:
        storage = []
        for y in x:
            if y != None:
                storage.append(y)
        print(" ".join(list(map(str,storage))))
# end = time.time()
# print(f"執行時間: {end - start : .5f}")