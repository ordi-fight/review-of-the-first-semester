
class Potato:
    def __init__(self) :
        self.i = 0
        self.j = 0
        self.score = 0
    def play(self , time , maze):

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

        return f"Potato arrives at ({self.i},{self.j}) when t={time}"
    def get_summary_message(self,time):

        return f"Potato spent {time} seconds and get {self.score} points"

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
