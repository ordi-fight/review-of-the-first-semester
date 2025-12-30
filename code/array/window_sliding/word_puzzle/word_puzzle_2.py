S = list(input())
k = int(input())   # the size of window
T = input()  
if k == 0 and T == "":
    print("YES")
    exit()
elif k == 0 and T != "":
    print("NO")
    exit()

from collections import Counter 

counter_T = Counter(T)
window = Counter(S[:k])

if all(window[m] >= counter_T[m] for m in counter_T) :
    print("YES")
    exit()

output = False

for i in range(k,len(S)):           # start from k to minimize the count of loop

    left = S[i-k]
    right = S[i]
    window[left] -= 1
    
    if window.get(right,0) :
        window[right] += 1
    else:
        window[right] = 1 

    if all(window[m] >= counter_T[m] for m in counter_T) :
        output = True
            
print("YES" if output else "NO")


# worse case O(n*n)
# when testcase is infinite , we can't use any loop
# the reason of very slow is we have to make dict as window not list

