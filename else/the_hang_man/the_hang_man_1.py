n = int(input())
k = int(input())
ans = input()
chance = k
def check(ori,c,ans):
    for i,j in enumerate(ans):
        if c == j :
            ori = ori[:i] + c + ori[i+1:]
    return ori
def guess(word,ans):
    if word == ans:
        return "You win"
    else:
        return "Wrong"
def hint(ori,ans):
    for i,j in enumerate(ans):
        if i == ans[0] :
            ori = ori[:i] + c + ori[i+1:]
    return ori
oper = []
while True:
    try:
        oper.append(input().split())
    except EOFError:
        break
ori = "_"*n
count = 0
for i in oper:
    if i[0] == "check":
        ori = check(ori,i[1],ans)
        print(ori)
        chance -= 1
    if i[0] == "guess":
        print(guess(i[1],ans))
        if guess(i[1],ans) == "You win":
            exit()
        chance -= 1
    if i[0] == "hint":
        if count == 0:
            print(hint(ori,ans))
            chance -= 1
        else:
            print("Aready used")
        count += 1
    if i[0] == "chance":
        print(chance)
    if chance == 0:
        print("You lose")
        exit()
# 在視覺頁面中的_ _ 在bash中會合起來