string = input()

dic = {
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T' ,'U', 'V'],
    9: ['W', 'X', 'Y', 'Z'],
}

time = 0

for i in range(len(string)):
    for j in dic.keys():
        if string[i] in dic[j]:
            time += (2 + (j - 1))
            
print(time)