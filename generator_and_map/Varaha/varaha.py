list = {}

def add(L):
  
  
  if L[0] in list:
    
    list[L[0]] += int(L[1])
    
  else:
    
    list[L[0]] = int(L[1])

def remove(R):
  
  
  list[R[0]] -= int(R[1])

  if list[R[0]] <= 0:
    
    del list[R[0]]
    
def show():
  
  print(list)
  
def count():
  
  count = 0
  
  for i in list.values():
    count += i
    
  print(count)

def clear():
  
  list.clear()
  
  
actions = {"add" : add, "remove" : remove, "show" : show , "count" : count, "clear" : clear }


n = int(input())

for _ in range(n):
  
  cmd = input().strip()
  
  if cmd == "add" or cmd == "remove":
    
    L = input().split()
    
    actions.get(cmd)(L)
    
  else:
    
    actions.get(cmd)()
