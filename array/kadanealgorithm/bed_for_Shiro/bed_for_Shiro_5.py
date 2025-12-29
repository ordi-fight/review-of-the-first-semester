
T = int(input())
for i in range(2*T) :                                  
    array = list(map(int,input().split()))

    if (i % 2) == 1 :
        S = list(sum(array[0:j+1]) for j in range(len(array)))
        if len(S) == 1:
            print(S[0])
            continue
        if max(array) < 0:
            print(max(array))
            continue
        min_ind = S.index(min(S))
        max_ind = S.index(max(S))
        min_val = min(S)
        max_val = max(S)
        if min_ind < max_ind:
            print(max_val - min(0,min_val))
        elif min_ind > max_ind :
            if max_ind == 0 and min_ind == len(S) - 1:
                print(max_val)
            elif max_ind > 0 and min_ind < len(S) - 1:
                S = [0] + S + [S[len(S)-1]]
                print(max(max_val - min(S[:max_ind+1]),max(S[min_ind+2:]) - min_val )) 
            elif max_ind == 0 and min_ind < len(S) -1 :
                S = S + [S[len(S)-1]]
                print(max(max_val,max(S[min_ind+2:]) - min_val))
            else:
                S = [0] + S
                print(max_val - min(S[:max_ind+1]))
    else:
        continue
    

# 分支可能太多造成程式混亂出錯超時
