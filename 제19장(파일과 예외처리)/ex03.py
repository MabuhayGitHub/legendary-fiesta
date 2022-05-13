#   파일 닫기

# close()
file = open("C:/Python/Inflearn/python/제19장(파일과 예외처리)/test.txt", "r", encoding="UTF-8")
line = file.readline().rstrip()
print(line)
file.close()

# try~finally
try:
    file = open("C:/Python/Inflearn/python/제19장(파일과 예외처리)/test.txt", "r", encoding="UTF-8")
    line = file.readline().rstrip()
    print(line)
finally:    # 무조건 실행
    file.close()

# with open ~ as  
# 명령문 내의 블럭이 종료될 때 파일은 자동으로 닫힘
with open("C:/Python/Inflearn/python/제19장(파일과 예외처리)/test.txt", "r", encoding="UTF-8") as file:
    line = file.readline().rstrip()
    print(line)