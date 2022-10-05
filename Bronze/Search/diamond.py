import os
import sys
sys.stdin = open("diamond.in", "r")
sys.stdout = open("diamond.out", "w")
n, k = map(int, input().split())
massive = []
for j in range(n):
    massive.append(list(map(int, input().split())))
cnt = 0
cnt2 = 0
for i in range(n - 1):
    for j in range(n):
        if (massive[j][0] >= massive[i][0] and massive[j][0] <= massive[i][0] + k):
            cnt += 1
    cnt2 = max(cnt, cnt2)
    cnt = 0
print(cnt2)
