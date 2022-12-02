import math
a = open('/Users/aadrijupadya/Desktop/USACO/Bronze/AOC/day1.txt', 'r')
nums = []

for i in a:
    nums.append(i.strip())
sums = []
cnt = 0

for i in nums:
    if i == '':
        sums.append(cnt)
        cnt = 0

    else:
        cnt += int(i)
sums = sorted(sums)
print(sums[-1] + sums[-2] + sums[-3])
