# try:
#     n = int(input("정수를 입력하세요: "))
# except ValueError:
#     print("입력값이 올바르지 않습니다")

# -----------------------------------------------------

# path = "C:/Python/Inflearn/python/제19장(파일과 예외처리)/files/"
# filename = path + "uscons.txt"
# try:
#     infile = open(filename, "a")
#     infile.write("파일 내용 기재")
# except FileNotFoundError:
#     print("파일이 존재하지 않습니다")
# else:
#     print("파일에 성공적으로 기록했습니다")
# finally:
#     infile.close()

# -----------------------------------------------------

raise NameError("이름이 잘못 되었습니다")