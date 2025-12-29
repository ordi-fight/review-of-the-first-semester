class Potato:
    def __init__(self) :
        self.i = 0
        self.j = 0
        self.score = 0
    def play(self , time , maze):

        maze.update_time(time,self)

        self.score += maze.pick_up_treasure_at(self.i,self.j)

        if maze.is_cell_walkable(self.i,self.j+1):

            self.j += 1
        elif maze.is_cell_walkable(self.i+1,self.j):

            self.i += 1
        elif maze.is_cell_walkable(self.i,self.j - 1):

            self.j -= 1
        elif maze.is_cell_walkable(self.i - 1,self.j ):

            self.i -= 1

    def get_location_message(self,time):

        return f"Potato arrives at {(self.i,self.j)} when t={time}"
        
    def get_summary_message(self,time):
        #output form
        return f"Potato spent {time} seconds and got {self.score} points"
        
class MazeRotatingEvent:
    def __init__(self,t,i,j,w,d):
        self.t = t
        self.i = i
        self.j = j
        self.w = w
        self.d = d

class maze:
    def __init__(self,n,m):

        self.n = n
        self.m = m
    def read_grid(self):
        self.grid = [list(map(int,input().split())) for i in range(self.n)]
        # print(self.grid)
    def read_k_events(self,k):

        self.events = dict()
        for i in range(k):
            t,i,j,w,d = map(int,input().split())
            rotatingEvent = MazeRotatingEvent(t,i,j,w,d)
            self.events[t] = rotatingEvent
        
    def is_call_the_end(self,i,j) :

        return (i,j) == (self.n - 1,self.m - 1 )
    def is_cell_walkable(self,i,j):
        
        return  (0 <= i < self.n and 0 <= j < self.m) and self.grid[i][j] >= 0 

    def pick_up_treasure_at(self,i,j):

        treasure = self.grid[i][j] 

        self.grid[i][j] -=  1

        return treasure

    def update_time(self,time,potato):
        # define the valuable then you can use it
        potato_posi_i_new = potato.i
        potato_posi_j_new = potato.j

        if time in self.events:

            r_center_x = self.events[time].i 
            r_center_y = self.events[time].j
        
            relative_x = r_center_x -  (self.events[time].w // 2)
            relative_y = r_center_y -  (self.events[time].w // 2)

            temp = [[None]*self.events[time].w for _ in range(self.events[time].w)]
            for x in range(self.events[time].w):
                for y in range(self.events[time].w):
                    if self.events[time].d == 0:
                        temp[y][self.events[time].w - 1 - x] = self.grid[relative_x + x][relative_y + y]

                        if relative_x + x == potato.i and relative_y + y == potato.j:
                            potato_posi_i_new = (potato.j - relative_y) + relative_x
                            potato_posi_j_new = (self.events[time].w - 1) - (potato.i - relative_x) + relative_y 

                        #  the wrong versrion
                        #  if 0 <= potato.i - relative_x < self.events[time].w and 0 <= potato.i - relative_y < self.events[time].w:
                        #  ... change ，then this condition will match finite time(as many as self.events[time].w) and potato move in the loop 
                        # and the potato move to the wrong position . Then, the anwser while loop can't break
                    elif self.events[time].d == 1:
                        temp[self.events[time].w - 1 - y][x] = self.grid[relative_x + x][relative_y + y]
                        if relative_x + x == potato.i and relative_y + y == potato.j:
                            potato_posi_i_new = (self.events[time].w - 1) - (potato.j - relative_y) + relative_x
                            potato_posi_j_new = (potato.i - relative_x) + relative_y 
                        #potato_posi_i_new is local valuable if you want to use it outside the if condition suit，you have to define it outside 
            for x in range(self.events[time].w):
                for y in range(self.events[time].w):
                    self.grid[relative_x + x][relative_y + y] = temp[x][y]

            potato.i = potato_posi_i_new
            potato.j = potato_posi_j_new

n,m,k = map(int,input().split())

magic_maze = maze(n,m)

magic_maze.read_grid()
magic_maze.read_k_events(k)

cute_potato = Potato()

time = 0
while True:
    old_i, old_j = cute_potato.i , cute_potato.j

    cute_potato.play(time , magic_maze)

    print(cute_potato.get_location_message(time))

    if magic_maze.is_call_the_end(cute_potato.i, cute_potato.j):

        print(cute_potato.get_summary_message(time))

        break

    time += 1