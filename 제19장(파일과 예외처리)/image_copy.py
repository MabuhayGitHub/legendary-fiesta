path = "C:/Python/Inflearn/python/제19장(파일과 예외처리)/files/"
ifilename = path + "fingerheart.png"
ofilename = path + "newfingerheart.png"


infile = open(ifilename, "rb")
outfile = open(ofilename, "wb")

while True:
    copy_buffer = infile.read(1024)
    if not copy_buffer:
        break
    outfile.write(copy_buffer)

infile.close()
outfile.close()