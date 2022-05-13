import time

path = "C:/Python/Inflearn/python/제19장(파일과 예외처리)/files/"
filename = path + "_sss.txt"

infile = open(filename, "r", encoding="UTF-8")
ch = infile.read(1)
# print(ch)
while ch != "":
    print(ch, end="")
    time.sleep(0.05)
    ch = infile.read(1)
infile.close()
