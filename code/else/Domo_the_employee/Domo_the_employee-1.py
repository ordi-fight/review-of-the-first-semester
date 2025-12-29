# save the index list and it can be subtracted some integer
index = list(map(int,input().split()))

#generate a two dimention list of information
while True:
    try:
        infro = input().split(",")
    except :
        break
# print(len(infro))    
#pull out the infro that I don't want according to index

    buf = []
    for inds in index:
        if inds < len(infro):
            buf.append(infro[inds])     #the return is None
    print(",".join(buf))


         






