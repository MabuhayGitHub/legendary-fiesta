#   파일 열기

# file = open("C:\\Python\\Inflearn\\python\\제19장(파일과 예외처리)\\test.txt", "r", encoding="UTF-8")
file = open("C:/Python/Inflearn/python/제19장(파일과 예외처리)/test.txt", "r", encoding="UTF-8")

line = file.readline().rstrip() # rstrip() 함수를 사용하여 \n 제거

while line != "":
    print(line)
    line = file.readline().rstrip()

file.close()
