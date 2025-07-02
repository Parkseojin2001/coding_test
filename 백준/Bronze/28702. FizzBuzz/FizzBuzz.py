import sys


sentence = []
last = 'Unknown'
index = -1

for i in range(3):
    s = sys.stdin.readline().rstrip()
    sentence.append(s)
    
    if s != 'Fizz' and s != 'Buzz' and s != 'FizzBuzz':
        index = i

number = int(sentence[index])
number += 3 - index

if number % 15 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print(str(number))