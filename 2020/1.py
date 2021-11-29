#!/us/bin/env python3

#I'm REALLLY REAL?Y RUSTY WITH PYTHON
def search_list(lines: list,total: int): 
    for line in lines:
        wanted = total - line
        if wanted in lines: 
            total = wanted * line
            print(f"{line},{wanted}")
            print(f"{total}")
            return  total
    return 0

lines = []

with open('1.in') as f:
    for line in f:
        lines.append(int(line))
total = 0
for line in lines: 
    total = search_list(lines,2020 - line) * line;
    if total > 0: 
        break

print(f"{total}")
