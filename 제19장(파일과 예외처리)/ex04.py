#   파일 읽기
# read()        파일의 모든 내용 읽기
# readline()    한 라인씩 읽기
# readlines()   여러 라인을 리스트에 저장(빈칸, 개행 포함)

filepath = "C:/Python/Inflearn/python/제19장(파일과 예외처리)/"
ifile = filepath + "test.txt"
with open(ifile, "r", encoding="UTF-8") as infile:
    string = infile.read()
    print(string)



filepath = "C:/Python/Inflearn/python/제19장(파일과 예외처리)/"
ifile = filepath + "test.txt"
with open(ifile, "r", encoding="UTF-8") as infile:
    string = infile.readline().rstrip()
    while string != "":
        print(string)
        string = infile.readline().rstrip()



filepath = "C:/Python/Inflearn/python/제19장(파일과 예외처리)/"
ifile = filepath + "test.txt"
with open(ifile, "r", encoding="UTF-8") as infile:
    list = infile.readlines()
    print(type(list))
    print(list)
    string = "".join(list)
    print(string)
        
