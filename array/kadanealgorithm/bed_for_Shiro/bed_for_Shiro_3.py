
T = int(input())
for i in range(2*T) :                                  
    array = list(map(int,input().split()))

    if (i % 2) == 1 :
        S = list(sum(array[0:i+1]) for i in range(len(array)))
        if len(S) == 1:
            print(S[0])
            continue
        S = [0] + S
        ans = []
        for m,n in enumerate(S):
            if len(S[:m]) > 1:
                # print(S[:m])
                ans.append(n - min(S[:m]))
            elif len(S[:m]) == 1:
                ans.append(n)
        print(max(ans))
        
    else:
        continue
    


