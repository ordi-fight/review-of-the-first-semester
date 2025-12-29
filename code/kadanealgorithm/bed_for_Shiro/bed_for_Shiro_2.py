
T = int(input())
for i in range(2*T) :                                  
    try:
        array = list(map(int,input().split()))

        if (i % 2) == 1 :
            S = list(sum(array[0:i+1]) for i in range(len(array)))
            # print(S)
            min_S = min(S)
            max_S = max(S)
            S = [0] + S
            output_1 = output_2 = -100
            if S[0:S.index(max_S)] :
                # print(S)
                output_1 = max_S - min(S[0:S.index(max_S)])
                # print(f"{output_1} is output_1")
            if S[S.index(min_S)+1:] :
                output_2 = max(S[S.index(min_S)+1:]) - min_S
                # print(f"{output_2} is output_2")
            if S[0:S.index(min_S)]:
                output_3 = min_S - min(S[0:S.index(min_S)])
                # print(f"{output_3} is output_3")

            if len(S) == 1:
                output = S[0]
            else:                                                                  #
                output = max([output_1,output_2,output_3])
                print(output,end = "\n")                                                            # Python 變數只有在對應分支執行時才會定義 #如果第一種情況即對，他不會跑其他在做比較
               
        else:
            continue
                
    except EOFError:
        break


