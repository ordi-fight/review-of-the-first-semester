S = list(input())
k = int(input())
T = input()

output = False
count = 0
num_loop = 0
m = 0

from collections import Counter
T_counter  = Counter(T)
T_counter_2  = T_counter.copy()               #they have different id
for i, j in enumerate(S):                       
    
    if T_counter[j] > 0 and j == S[i-m] :
        T_counter[j]-= 1
        count += 1
    num_loop += 1
    
    if count == len(T):
        if num_loop <= k and len(T) <= k :  #<- big bug
            print("YES")
            output = True
            break
        elif num_loop >= k:
            m = num_loop
            count -= 1
            if T_counter_2[S[i-m]] > 0:
                num_loop = m -1
            else:
                num_loop = m -2
            T_counter = T_counter_2
            continue
        
if not output :
     
    print("NO")