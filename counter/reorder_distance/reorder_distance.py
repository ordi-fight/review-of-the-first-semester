s = list(input())
t = list(input())

from collections import Counter               # a dict that value is keys' quantity
t_counter = Counter(t)
count = 0
for i in s:
    if t_counter[i] > 0 :  #O(1)                  # key is i and value is quantity
        count += 1
        t_counter[i] -= 1   #O(1)
print(len(s) - count)



# in and remove are linear search so the BigO is O(n)
# so if I use "in" the total Big O is O(n*n)+ n + n(input) n*(n+n) (for,in,remove)
#if I change t into "Counter" dict (a dict that value is keys' quantity) BigO is O(n)
# the total is O(n+n)