def extract_columns(csv: str, indices: str):
    
    query = list(map(int,indices.split()))

    for line in csv.split("\n"):
        line = line.split(",")
        buf = list(line[x] for x in query)
        yield ",".join(buf)
    


# Read the CSV input until EOF
csv_lines = []
while True:
    try:
        line = input()
        if line.strip() == "":
            continue
        csv_lines.append(line)
    except EOFError:
        break
# First line = indices
ind_line = csv_lines[0]
ind = list(map(int, ind_line.split()))

# Remaining lines = CSV data
csv_str = "\n".join(csv_lines[1:])

# Process
for i in extract_columns(csv_str, ind_line):   #extract_columns(csv_str, ind_line) is a generator ，so i is to take the value that throw out by yield
    print(i)