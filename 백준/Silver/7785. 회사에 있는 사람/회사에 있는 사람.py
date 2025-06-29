n = int(input())

logs = set()

for _ in range(n):
    name, state = map(str, input().split())
    if state == 'enter':
        logs.add(name)
    elif state == 'leave':
        logs.discard(name)
    else:
        print("Error")

logs = list(logs)

logs.sort(reverse=True)

for log in logs:
    print(log)