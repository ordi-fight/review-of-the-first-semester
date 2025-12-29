T = int(input())
for i in range(T*2):

    array = list(map(int,input().split()))

    if (i % 2) == 1 and array :
        # print(array)
        global_max = array[0]
        current_max = array[0]

        for i in array[1:]:                           #array[0]已經讀過了
            
            current_max = max(i,current_max + i)
            global_max = max(global_max,current_max)
            # print(current_max,global_max)
        print(global_max)
    else:
        continue

