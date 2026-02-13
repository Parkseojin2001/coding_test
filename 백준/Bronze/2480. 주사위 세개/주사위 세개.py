dice = list(map(int, input().split()))

money = 0


if len(set(dice)) == 1:
    money += 10000 + dice[0] * 1000
    
elif len(set(dice)) == 2:
    money += 1000 + (sum(dice) - min(dice) - max(dice)) * 100
else:
    money += max(dice) * 100
        
print(money)