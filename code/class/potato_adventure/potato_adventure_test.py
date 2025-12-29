t,i,j,w,d = 1, 2, 2, 3, 1

r_center_x = i
r_center_y = j

potato_posi_i = 1 
potato_posi_j = 2

grid = [[0,1,0,0,0],[0,1,2,3,0],[0,4,5,6,0],[0,7,8,9,0],[0,0,0,0,0]]

relative_x = r_center_x -  (w // 2)
relative_y = r_center_y -  (w // 2)

temp = [[None]*w for _ in range(w)]
potato_posi_i_new = potato_posi_i
potato_posi_j_new = potato_posi_j

for y in range(5):
    for x in range(5):
        print(grid[y][x], end=' ')
    print()    

for x in range(w):
    for y in range(w):
        if d == 0:
            temp[y][w - 1 - x] = grid[relative_x + x][relative_y + y]

            if relative_x + x == potato_posi_i and relative_y + y == potato_posi_j:
                potato_posi_i_new = (potato_posi_j - relative_y) + relative_x
                potato_posi_j_new = (w - 1) - (potato_posi_i - relative_x) + relative_y 

        elif d == 1:
            temp[w - 1 - y][x] = grid[relative_x + x][relative_y + y]
            if relative_x + x == 0 and relative_y + y == 2:
                potato_posi_i_new = (w - 1) - (potato_posi_j - relative_y) + relative_x                    
                potato_posi_j_new = (potato_posi_i - relative_x) + relative_y 
for x in range(w):
    for y in range(w):
        grid[relative_x + x][relative_y + y] = temp[x][y]

i = potato_posi_i_new
j = potato_posi_j_new
print()

for y in range(5):
    for x in range(5):
        print(grid[y][x], end=' ')
    print()   

print(i,j)


# def pick_up_treasure_at(i,j):
#         treasure = grid[i][j] 
#         grid[i][j] -=  1
#         return treasure

# score = 0
# for i in range(4):
#     for j in range(4):
#         if grid[i][j] > 0 :
#             score += pick_up_treasure_at(i,j)
# print(score,grid)

