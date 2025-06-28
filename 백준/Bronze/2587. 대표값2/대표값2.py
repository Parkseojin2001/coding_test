scores = []

for i in range(5):
    scores.append(int(input()))

scores.sort()

print(int(sum(scores) / 5))
print(scores[2])