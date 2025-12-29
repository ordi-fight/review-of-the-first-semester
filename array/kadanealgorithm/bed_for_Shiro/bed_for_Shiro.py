T = int(input())
array_A = []
while True:
    try :
            array_A.append(list(map(int,input().split())))

    except EOFError:
        break


for i in range(1,len(array_A),2):

        if  max([ k for k in array_A[i]]) <= 0:
                orig_sum = max([ k for k in array_A[i]])
        else:
                orig_sum = 0
                for r1 in range(len(array_A[i])):
                        for r2 in range(len(array_A[i])-1,-1,-1):
                                if r2 >= r1:
                                        if sum(array_A[i][r1:r2+1]) >=  orig_sum:
                                                orig_sum = sum(array_A[i][r1:r2+1])
        print(orig_sum)
     
# print(array_A)