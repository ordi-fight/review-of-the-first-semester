class PendingTaskIterator:
    def __init__(self,task_queue):
        self.pending = list(filter(lambda task: task["done"] == False,task_queue[:]))
        print(type(task_queue[:]))
        print(type(task_queue))
        self.index = 0



    def __next__(self):
        # TODO:
        
        if self.index >= len(self.pending):
          raise StopIteration
        else:
        
            val = self.pending[self.index]

            self.index += 1
            return val
          
                

class TaskQueue(list):
    # Taskqueue inherit from list ，the instance of Taskqueue can do any methid of list
    # the instance of Taskqueue is equal to [ ] on tje implementation level 
    # but the type of the two objects are different    
    def add_task(self, name):
        # TODO:
        # Append a new task dict to the list.
        self.append({"name":name, "done": False})
      
        

    def mark_done(self, name):
        # TODO:
        # Traverse the underlying list in insertion order

        
        for  task in self:
            print(self)
            if task["name"] == name : 
            

                task["done"] = True
                break
            print("hello")

            
    def __iter__(self):
        # TODO:
        # Return a PendingTaskIterator for this TaskQueue
        
        return PendingTaskIterator(self)


""" Do not change the code below """

# q = int(input())
tq = TaskQueue()
while True:
    op = input().split()

    if op[0] == "ADD":
        name = " ".join(op[1:])
        tq.add_task(name)

    elif op[0] == "DONE":
        name = " ".join(op[1:])
        tq.mark_done(name)

    elif op[0] == "LEN":
        print(len(tq))

    elif op[0] == "PRINTALL":
        print(tq)

    elif op[0] == "PENDING":
        k = int(op[1])
        it = iter(tq)
        for _ in range(k):
            
            print(next(it))