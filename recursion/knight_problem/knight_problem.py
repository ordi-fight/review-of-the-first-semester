m,n = map(int,input().split())   #input

moving_order = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

matrix = []
for i in range(m):
  matrix.append([0]*n)
i = 0
j = 0
step_index = 0
start_step = 0
count = -1
step_list = []
def knight(m,n,moving_order,matrix,start_step,step_list,step_index,i,j,count):
  for x , y in moving_order[start_step:]:
    judgement = False
    c = i
    d = j
    c += x
    d += y
    count += 1
    if matrix[c][d] == 0 and 0<= c <m and 0<= d < n:
      step_list.append(count + 1)
      step_index += 1
      matrix[c][d] = step_index
      count = -1
      judgement = True
      break
  if not judgement:
    matrix[i][j] = 0
    count = -1
    start_step = step_list[step_index-1]
    step_list = step_list[:len(step_list)-1]   #把原本那個用的第幾步刪掉，以便在加新的，可以使step_index和step_list吻合，這較合理  
  matrix = knight(m,n,moving_order,matrix,start_step,step_list,step_index,i,j,count)
  return matrix
print(knight(m,n,moving_order,matrix,start_step,step_list,step_index,i,j,count))


#Incorrect Position Handling
#No Base Case -> infinite recurtion
#Backtracking Logic


m, n = map(int, input().split())  # input

moving_order = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

matrix = []
for i in range(m):
    matrix.append([0] * n)
i = 0
j = 0
step_index = 0
start_step = 0
count = -1
step_list = []  # 儲存 (move_idx, i, j)

def knight(m, n, moving_order, matrix, start_step, step_list, step_index, i, j, count):

    for move_idx, (x_move, y_move) in enumerate(moving_order[start_step:], start=start_step):
      c = i
      d = j
      c = i + x_move
      d = j + y_move
      if 0 <= c < m and 0 <= d < n and matrix[c][d] == 0:
        step_list.append((move_idx + 1, i, j))
        step_index += 1
        matrix[c][d] = step_index
        i = c
        j = d
        matrix = knight(m, n, moving_order, matrix, 0, step_list, step_index, c, d, count)

    if step_index > 0:
        prev_move_idx, i, j = step_list.pop(step_index - 1)
        matrix[i][j] = 0
        start_step = prev_move_idx
        step_index -= 1
        matrix = knight(m, n, moving_order, matrix, start_step, step_list, step_index, prev_x, prev_y, count)
    else:
        return matrix