L = input().split(", ")

month_map = { 'Jan': "01", 'Feb': "02", 'Mar': "03", 'Apr': "04", 'May': "05", 'Jun': "06", 'Jul': "07", 'Aug': "08", 'Sep': "09", 'Oct': "10", 'Nov': "11", 'Dec': "12" }

def month_mapping(M):
  if M in month_map:
    
    return month_map[M]

def format(i):
  
  if "-" in i : 
    
    return  tuple([i.split("-")[0],i.split("-")[1],i.split("-")[2]])
  
  if "/" in i :
    
    return  tuple([i.split("/")[2],i.split("/")[0],i.split("/")[1]])
    
  if " " in i :
    
    return  tuple([i.split()[2],month_mapping(i.split()[1]),i.split()[0]])


L.sort(key = lambda s: format(s))

print("\n".join(L))