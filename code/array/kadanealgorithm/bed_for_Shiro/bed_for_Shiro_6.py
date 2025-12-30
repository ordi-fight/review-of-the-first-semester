T = int(input())
for i in range(T*2):

    array = list(map(int,input().split()))
    
    if (i % 2) == 1 and array :
        
        prefix = 0
        prefix_min = 0
        max_sum = array[0]
        for j in array:
            prefix += j
            max_sum = max(max_sum,prefix - prefix_min)
            prefix_min = min(prefix,prefix_min)
        print(max_sum)
    else:
        continue