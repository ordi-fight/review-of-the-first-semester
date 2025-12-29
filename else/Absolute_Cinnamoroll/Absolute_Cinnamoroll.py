T = int(input())
possi_kinds = 0
for k in range(1,T) :
    m = k
    # n = k a*b*c = k   ask the possibility of (a,b,c)
    # count the primer 
    if k % 2 == 0:
        n = (k & -k).bit_length() - 1 
        k = k // (k & -k)                # string can't include & and n & -n will be inteprete as 4 (int)

    if k == 1 and m != 1:
        # possi_kinds = 0
        for i in range(n+1):
            # print(i)
            possi_kinds += (n - i + 1)
            # print(possi_kinds) 
    if k != 1 or m == 1:
        import math
        prime = []       
        for i in range(1,m+1):
            if m % i == 0:
                prime.append(i)        #[1,3] #[1]
        # print(prime)
        # if int(m**0.5) == m**0.5:
        #     count = len(prime)*2 + 1
        # else:
        #     count = len(prime)*2
        # print(count)
        # the possibility of (a,b,c)
        # possi_kinds = 0
        prime_2 = list(reversed(prime))
        for i,f in enumerate(prime_2):                                 # i is index and f is item
            for j in prime[:len(prime)-i]:
                if f % j == 0:
                    possi_kinds += 1 
    # print(m,possi_kinds)
            
print(possi_kinds)

#nearly 10^3 ok
