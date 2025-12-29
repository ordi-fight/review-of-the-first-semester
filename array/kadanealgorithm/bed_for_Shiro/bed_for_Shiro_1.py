T = int(input())  # the question has tell you how many testcases you have, don't be limited by try except 

for i in range(2*T) :                                  # i 1 3 5
    try:
        array = list(map(int,input().split()))

        if (i % 2) == 1 :
            if array and max(array) <= 0:
                print(max(array))
            else:
                orig_sum = 0
                for r1 in range(len(array)):
                    for r2 in range(len(array)-1,-1,-1):
                        if r2 >= r1:
                            if sum(array[r1:r2+1]) >=  orig_sum:
                                orig_sum = sum(array[r1:r2+1])
                print(orig_sum)
        else:
            continue
                
    except EOFError:
        break
          
   # there are  2 ^ 500000 possible subset so oj say time exceeded limit  


           


     
