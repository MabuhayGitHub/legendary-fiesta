#   sales.txt

# infilename = input("입력 파일명: ")
# outfilename = input("출력 파일명: ")
# filepath = "C:/Python/Inflearn/python/제19장(파일과 예외처리)/"
# ifile = filepath + infilename
# with open(ifile, "r", encoding="UTF-8") as infile:

sum = 0
count = 0


with open("C:/Python/Inflearn/python/제19장(파일과 예외처리)/sales.txt", "r", encoding="UTF-8") as infile:
    line = infile.readline().rstrip()
    while line != "":
        sales_num = int(line)
        sum += sales_num
        count += 1
        print(count, sum)
        line = infile.readline().rstrip()

with open("C:/Python/Inflearn/python/제19장(파일과 예외처리)/summary.txt", "w", encoding="UTF-8") as outfile:
    outfile.write("총매출 = " + str(sum) + "\n")
    outfile.write("평균 일매출 =" + str(sum/count))
