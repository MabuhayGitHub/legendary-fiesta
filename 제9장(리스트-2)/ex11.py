# s = [   [ 1,  2,  3,  4,  5], 
#         [ 6,  7,  8,  9, 10], 
#         [11, 12, 13, 14, 15]]

# for i in range(len(s)):
#     print(id(s[i]))
#     for j in range(len(s[i])):
#         # print(s[i][j], end="\t")
#         print(id(s[i][j]), end="\t")
#     print("")

# ########################################################################

# rows = 3
# cols = 5
# s = []

# for row in range(rows):
#     s += [[0] * cols]
# print(s)

# ########################################################################

# s = [   [ 1,  2,  3,  4,  5], 
#         [ 6,  7,  8,  9, 10], 
#         [11, 12, 13, 14, 15]]

# sum1 = 0
# for i in range(len(s[0])):
#     sum1 += s[0][i]
# print(sum1)

# ########################################################################

# s = [   
#         [ 1,  2,  3,  4,  5], 
#         [ 6,  7,  8,  9, 10], 
#         [11, 12, 13, 14, 15]
#     ]

# for i in range(len(s)):
#     for j in range(len(s[i])):
#         print(s[i][j], end="\t")
#     print()

# ########################################################################

rows = int(input("행의 갯수: "))
cols = int(input("열의 갯수: "))

dbl_list = []

for row in range(rows):
    # dbl_list += [[0] * cols]
    dbl_list = [ ([0] * cols) for row in range(rows)]
print(dbl_list)    
