# import math
# n = int(input())
# metalist = []
# for i in range(n):
#     a = input().split()
#     metalist.append(a)

# for i in metalist:
#     liars = 0
#     for a,b in i:
#         if a == 'G':
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
