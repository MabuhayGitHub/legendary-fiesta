# 정규식

import re

# path = "C:/Python/Inflearn/python/제19장(파일과 예외처리)/files/"
# filename = path + "uscons.txt"

# file = open(filename, "r")
# for line in file:
#     line = line.rstrip()
#     if re.search("^[0-9]+", line):
#         print(line)

text = """
101 COM Python Program
102 MAT LinearAlgebra
103 ENG Computer
"""
print(text)

s = re.findall("\d+", text)
print(s)