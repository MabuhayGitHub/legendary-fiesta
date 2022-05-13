path = "C:/Python/Inflearn/python/제19장(파일과 예외처리)/files/"
filename = path + "mobydick.txt"

counter = [0] * 26
infile = open(filename, "r")
ch = infile.read(1)
while ch != "":
    ch = ch.upper()
    # if isalpha(ch):
    if ch >= "A" and ch <= "Z":
        i = ord(ch) - ord("A")
        counter[i] += 1
    ch = infile.read(1)
print(counter)
