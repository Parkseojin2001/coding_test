import sys         

input = sys.stdin.readline

line = input().strip()

line = line.replace('-', ' - ')
line = line.replace('+', ' ')

line = line.split(" ")

total = 0


i = 0

while i < len(line):
    plus_num = 0
    if line [i] == '-':
        i += 1
        while i < len(line) and line[i] != '-':
            plus_num += int(line[i])
            i += 1
        total -= plus_num
    else:
        total += int(line[i])
        i += 1
    
print(total)