class Student:
    def __init__(self, name, score, i, j):
        self.name = name
        self.score = score
        self.i = i
        self.j = j

    def set_score(self, score:int) -> None:
        # TODO set the new score for this student, and make sure the score is in valid range
        self = score

    def get_message(self) -> str:
        # TODO get the message by the required format
        return f"{self.name} at {(self.i,self.j)} scored {self.score}"

class PotatosClass:
    students = dict()

    def __init__(self, n, m):
        self.seats = [[None]*m for _ in range(n)]

    def record_students(self):
        for i in range(n*m):
            name, score, i, j = input().split()

            score, i, j = int(score), int(i), int(j)

            student = Student(name, score, i, j)
            self.students[name] = self.seats[i][j] = student

    def command_score(self, stu_name:str, new_score:int) -> None:
        self.students[stu_name].set_score(new_score)

    def command_rotate(self, i:int, j:int, width:int) -> None:
        # TODO rotate the student's seats
        temp = [[None]*width for _ in range(width)]
        for x in range(0,width):
            for y in range(0,width):
                temp[y][width-1-x] = self.seats[i+x][j+y]
    
                if temp[y][width-1-x]:
                    temp[y][width-1-x].i = i + y
                    temp[y][width-1-x].j = j + width-1-x
      
        for x in range(0,width):
            for y in range(0,width):  
                self.seats[i+x][j+y] = temp[x][y]
    def get_best_student(self,n,m) -> Student:
        # TODO get the best scored student
        basic_score = 0
        best_student = None
        for i in range(n):
            for j in range(m):
                if self.seats[i][j].score > basic_score:
                    basic_score = self.seats[i][j].score
                    best_student = self.seats[i][j].name
        return self.students[best_student]
n, m, k = map(int, input().split())

course = PotatosClass(n, m)
course.record_students()

for i in range(k):
    commands = input().split()

    if(commands[0] == "score"):
        course.command_score(commands[1], int(commands[2]))
    elif(commands[0] == "rotate"):
        course.command_rotate(int(commands[1]), int(commands[2]), int(commands[3]))

print(course.get_best_student(n,m).get_message())