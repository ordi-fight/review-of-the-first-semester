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
i = 0
while i < chance:
    oper = input().split()
    if oper[0] == "check":
        ori = check(ori,oper[1],ans)
        print(ori)
        chance -= 1
    if oper[0] == "guess":
        print(guess(oper[1],ans))
        if guess(oper[1],ans) == "You win":
            exit()
        chance -= 1
    if oper[0] == "hint":
        if count == 0:
            print(hint(ori,ans))
            chance -= 1
        else:
            print("Aready used")
        count += 1
    if oper[0] == "chance":
        print(chance)
print("You lose")