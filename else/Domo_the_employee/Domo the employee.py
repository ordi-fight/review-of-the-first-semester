#line = ""
#for raw_line in iter(input,""):
#       line = line +"\n" + raw_line
#ind_line = line[0:"\n"]
#ind = list(map(int, ind_line.split()))

csv_lines = []
while True:
    try:
        line = input()
        if line.strip() == "":
            continue
        csv_lines.append(line)
    except EOFError:
        break
ind = csv_lines[0]
inds = list(map(int,ind.split()))
menu = []
for x in csv_lines:
    menu.append( x.split(","))
print(menu)
for i in range(len(menu)):
        if i > 0:
            part = ""
            for k in inds: 
                 part = part + (menu[i])[k] + ","
            part = part.rstrip(",")
            print(part)

            












#output = ""
#for y in range(len(menu)) :
#    if 0 < y < len(menu):
#        if len(indices) ==1:
#            output = output + "\n" + menu[y][indices[0]] 
#        elif len(indices) ==2:
#            output = output + "\n" + menu[y][indices[0]] + "," + menu[y][indices[1]]
#        elif len(indices) ==3:
#            output = output + "\n" + menu[y][indices[0]] + "," + menu[y][indices[1]] + "," +  menu[y][indices[2]]
#print(output)
        

        
