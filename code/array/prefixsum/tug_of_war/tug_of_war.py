n = int(input())
k = int(input())
x = list(map(int,input().split()))

pre = 0
pre_list = [0]*abs(k)
cnt = 0
if k == 0:
  cnt = n + ((n)*(n-1))//2
else:
  for i in x :
    pre = ((pre + i) % abs(k))
    if pre == 0:
      cnt += 1
    cnt += pre_list[pre]
    pre_list[pre] += 1
    
print(cnt)