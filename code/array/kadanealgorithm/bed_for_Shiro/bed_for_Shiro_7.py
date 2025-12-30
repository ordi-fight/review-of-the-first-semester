t = int(input())
for _ in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    pre = [0] * (n)
    ans = pre[0] = ls[0]
    mn = min(0, pre[0])
    for i in range(1, n):
        pre[i] = pre[i - 1] + ls[i]
        if ans < pre[i] - mn:
            ans = pre[i] - mn
        if mn > pre[i]:
            mn = pre[i]
    print(ans)