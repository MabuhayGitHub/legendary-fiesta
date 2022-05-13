path = "C:/Python/Inflearn/python/제19장(파일과 예외처리)/files/"
filename = path + "proverbs.txt"

# inline = open(filename, "r", encoding="UTF-8")
# for line in inline:
#     line = line.rstrip()
#     word_list = line.split()
#     for word in word_list:
#         print(word)

# inline.close()

# -------------------------------------------------------------------------

# line = "apple,grape,banana,pear"
# word_list = line.split(",")
# print(word_list)
# for word in word_list:
#     print(word)

# -------------------------------------------------------------------------

infile = open(filename, "r")
ch = infile.read(1)
while ch != "":
    print(ch)
    ch = infile.read(1)

