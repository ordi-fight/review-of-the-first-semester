s = input()
k = int(input())
t = input()

if k > len(s):
    print("NO")
    exit()                                # speed up execute some special testscse
if k == 0 and t == "":
    print("YES")
    exit()
if k == 0 and t != "":
    print("NO")
    exit()
from collections import Counter

window = Counter(s[:k])
target = Counter(t)

def contain_target(window,target):          # judge if this window is the right one   the lengh of window_ini > len(T)
    for char , num in target.items():
        if window[char] < num:
            return False
    return True  

if contain_target(window,target):
    print("YES")
    exit()
else:
    for i in range(k,len(s)):
        right = s[i]
        left = s[i - k]
        window[left] -= 1
        if window[left] == 0:
            del window[left]
        if window.get(right,0) > 0 :
            window[right] += 1
        else:
            window[right] = 1
        if contain_target(window,target) :
            print("YES")
            exit() 
print("NO")

    
