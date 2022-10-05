import os
import sys
sys.stdin = open("Bronze/Search/pails.in", "r")
sys.stdout = open("Bronze/Search/pails.out", "w")
pail_list = list(map(int, input().split()))
quit = False
large = pail_list[2]
medium = pail_list[1]
small = pail_list[0]
cnt1 = 0
cnt2 = 0
maxValue = 0
while (cnt1 < large):
    cnt1 += small
while (cnt2 < large):
    cnt2 += medium
for i in range((large // small) + 1):
    j = large - i * small
    remainder = j % medium
    value = large - remainder
    print(value)
    if value > maxValue:
        maxValue = value


print(maxValue)
