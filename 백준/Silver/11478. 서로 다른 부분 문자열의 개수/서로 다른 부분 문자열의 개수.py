S = input()


set_S = set()

for i in range(len(S)):
    for j in range(1, len(S) - i + 1):
        set_S.add(S[i:i+j])
        
print(len(set_S))