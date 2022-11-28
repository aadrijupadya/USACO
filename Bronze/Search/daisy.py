n = int(input())
flowers = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i, n):
        avg_petals = sum(flowers[i:j + 1]) / len(flowers[i:j + 1])

        for index in range(i, j + 1):
            if flowers[index] == avg_petals:
                ans += 1
                break
print(ans)
