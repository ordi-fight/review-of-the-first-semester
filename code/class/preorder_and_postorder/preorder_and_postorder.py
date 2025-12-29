n = list(map(int,input().split()))
m = list(map(int,input().split()))

def pre(n,m):
  
  # construct index dict
  
  in_dict = {} 
  
  for i, j in enumerate(n):
    
    in_dict[j] = i
  
  
  root_index = in_dict[m[-1]]
  
  # left_subtree_len = root_index 
  
  # right_subtree_len = len(n) - root_index 
   
  
  if len(n) == 1 :
    
    # print(n)
    
    return n
    
    
  else:
    pre_output = []
    root  = m[-1]
    # print(root)
    try:
      l = pre(n[:root_index],m[:root_index])
    except :
      l = []
    try:
      
      r = pre(n[root_index+1:],m[root_index:len(m)-1])
      
    except:
      
      r = []
    
    pre_output.extend( [root] + l + r)
    # pre_output = pre_output + [root] +l+r
  
    return pre_output
    
print(" ".join(list(map(str,pre(n,m)))),end = " ")