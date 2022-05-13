# 파이썬 파일 현재 위치 확인 및 변경
# tell() 현재 위치 확인
# seek() 현재 위치 변경
# seek(0) 처음 위치로 이동

path = "C:/Python/Inflearn/python/제19장(파일과 예외처리)/"
filename = path + "test.txt"

file = open(filename, "r", encoding="UTF-8")
print("현재 위치", file.tell())
file.read()
print("현재 위치", file.tell())

print("-----------------------------------")

file.seek(0)
print("현재 위치", file.tell())

file.seek(5)
print(file.read(15))
