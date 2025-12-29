#you don't have to really know a*b*c = ? , and the only thing you have to verify is a*b*c < n - 1 and you indeed calculate how many (a,b,c) you have 
# ans = 0
# n = int(input())
# for a in range(1,n):
#     for b in range(1,n-1//a+1) :
#         for c in range(1,n-1//a*b+1) :
#             ans += 1 
ans = 0
n = int(input())
for a in range(1,n):
    for b in range(1,(n-1//a)+1) :
        ans += (n-1)//(a*b)
print(ans)