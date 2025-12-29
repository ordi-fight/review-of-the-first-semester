import ast
L = ast.literal_eval(input().strip())
dir_name = "root"
node_name =[]

def deletion(L,node_name):

  if type(L) is str:
    node_name.append(L)
  if type(L) is list and len(L) == 1:
    element = L[0]
    return f'Deleting /{"/".join(node_name)}/{element}\n'   #內圈 + \n
  output = "" 
  if type(L) is list and len(L) != 1:
    for i in L:
      output += f"{deletion(i,node_name)}"                     #外圈 + \n
    if len(node_name) > 1:
      output += f'Deleting /{"/".join(node_name)}\n'
      del node_name[-1]
  return output
if len(L) == 1:
    print(f"Deleting /{dir_name}")
else:
    print(f"{deletion(L,node_name)}Deleting /{dir_name}")
