s = [   
        [ 1,  2,  3,  4,  5], 
        [ 6,  7,  8,  9, 10], 
        [11, 12, 13, 14, 15]
    ]

sum1 = 0
for i in range(len(s[0])):
    sum1 += s[0][i]
print(sum1)

sum2 = 0
for i in range(len(s)):
    for j in range(len(s[i])):
        sum2 += s[i][j]
print(sum2)
