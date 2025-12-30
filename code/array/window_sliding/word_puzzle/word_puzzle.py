S = list(input())
k = int(input())
T = list(input())

v = []
inds = []



for i, j in enumerate(S):                       
    # print(i,j)
        
    if j in T :
        T.remove(j)                          
        inds.append(i)

    if T == []:
        if inds and (inds[len(inds)-1]-inds[0]+1) <= k:
            # print(inds)
            print("YES")
            break
        elif inds and (inds[len(inds)-1]-inds[0]+1) >= k:
            # print(inds)
            T = list(S[inds[0]])
            # print(T)
            inds = inds[1:]
            # print(inds)
            continue
        else: 
            print("NO")
            break
if T :
    # print(T) 
    print("NO")




# for loop is faster but can not go back
# while is too slow 
# part of the testcase will exceed the time limit