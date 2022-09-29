import sys
sys.stdin = open("mixmilk.in", "r")
sys.stdout = open("mixmilk.out", "w")
bucket_list = []
for i in range(3):
    bucket_list.append(list(map(int, input().split())))
# print(bucket_list)

# bucket1_capacity = bucket_list[0][0]
# bucket2_capacity = bucket_list[1][0]
# bucket3_capacity = bucket_list[3][0]

i = 0
j = 1
for n in range(100):

    if bucket_list[i][1] + bucket_list[j][1] <= bucket_list[j][0]:
        # if i == 1 and j == 2:
        #     temp = bucket_list[2][1] % bucket_list[0][0]
        #     bucket_list[2][1] = temp
        #     bucket_list[0][1] = bucket_list[2][1] - temp

        temp = bucket_list[i][1]
        bucket_list[j][1] = temp + bucket_list[j][1]
        bucket_list[i][1] = 0

    elif bucket_list[i][1] + bucket_list[j][1] > bucket_list[j][0]:
        temp = bucket_list[i][1] % bucket_list[j][0]
        bucket_list[j][1] = bucket_list[j][0]
        bucket_list[i][1] = temp

    i += 1
    j += 1

    if i == 2:
        j = 0

    if i > 2:
        i = 0


print(bucket_list[0][1])
print(bucket_list[1][1])
print(bucket_list[2][1])
# print(bucket_list)
