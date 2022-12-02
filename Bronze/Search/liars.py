
import math
pos = []
for i in range(int(input())):
    lg, val = input().split()
    pos.append([lg, int(val)])
print(pos)

ans = math.inf
for _, val in pos:
    print(val)
    liars = 0
    for lg, v in pos:
        print(v)
        if lg == 'G':
            if v > val:
                liars += 1
        elif lg == 'L':
            if v < val:
                liars += 1
    ans = min(ans, liars)
print(ans)
