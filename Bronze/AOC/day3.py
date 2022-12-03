a = open('/Users/aadrijupadya/Desktop/USACO/Bronze/AOC/day3.txt', 'r')
string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
text = []
letters = []
for i in a:
    text.append(i.strip())

# for i in text:
#     k = len(i)
#     str1 = i[0:k//2]
#     str2 = i[k//2:]
#     for j in str1:
#         if j in str2:
#             letters.append(j)
#             break
cnt = 0
sum = 0
for i in text:
    print(letters)
    if cnt < 2:
        letters.append(i)
    if cnt == 2:
        letters.append(i)
        for j in letters:
            for letter in j:
                if letter in letters[0] and letter in letters[1] and letter in letters[2]:
                    print(letter)
                    sum += (string.find(letter)+1)
                    break
        cnt = -1
        letters = []
    cnt += 1

print(sum/3)
