import math
a = open('/Users/aadrijupadya/Desktop/USACO/Bronze/AOC/day2.txt', 'r')
games = [i.strip() for i in a]

sum = 0
for i in games:
    if i[2] == "X":
        sum += 0
    if i[2] == "Y":
        sum += 3
    if i[2] == "Z":
        sum += 6
    if i[0] == "A" and i[2] == "X":
        sum += 3
    if i[0] == "A" and i[2] == "Y":
        sum += 1
    if i[0] == "A" and i[2] == "Z":
        sum += 2
    if i[0] == "B" and i[2] == "Y":
        sum += 2
    if i[0] == "B" and i[2] == "Z":
        sum += 3
    if i[0] == "B" and i[2] == "X":
        sum += 1
    if i[0] == "C" and i[2] == "Y":
        sum += 3
    if i[0] == "C" and i[2] == "Z":
        sum += 1
    if i[0] == "C" and i[2] == "X":
        sum += 2

print(sum)
