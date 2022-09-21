import sys
sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out", "w")
num_cases = list(map(int, input().split()))
total_cases = []
for i in range(num_cases[0]):
    total_cases.append(list(map(int, input().split())))
scores = []
for j in range(1, 4):
    pointer = j
    score = 0
    for i in range(len(total_cases)):
        guess = total_cases[i][2]
        if total_cases[i][0] == pointer:
            pointer = total_cases[i][1]
        elif total_cases[i][1] == pointer:
            pointer = total_cases[i][0]
        if guess == pointer:
            score += 1
    scores.append(score)


print(max(scores))
