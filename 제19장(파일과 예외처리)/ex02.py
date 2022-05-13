#   파일 쓰기

#   write/append 모드에서는 파일이 없을 경우 생성
file = open("C:/Python/Inflearn/python/제19장(파일과 예외처리)/input.txt", "w", encoding="UTF-8")
file.write("김수정")
file.close()

file = open("C:/Python/Inflearn/python/제19장(파일과 예외처리)/input.txt", "a", encoding="UTF-8")
file.write("신은혁")
print("박태환\n", file=file)
file.close()