# 파일 쓰기
# write() : \n 직접 입력 필요
# writelines() : 리스트 등 여러 문장 입력

path = "C:/Python/Inflearn/python/제19장(파일과 예외처리)/"
filename = path + "write_test.txt"

with open(filename, "w", encoding="UTF-8") as wfile:
    wfile.write("안녕하세요. 반갑습니다.\n")
    wfile.write("저는 홍길동입니다.\n")
    wfile.write("점심 식사 후 노곤함이 몰려오는 시간입니다.")

with open(filename, "a", encoding="UTF-8") as wfile:
    wfile.writelines(["하나", "둘", "셋", "넷", "다섯"])
    wfile.write("\n")
    wfile.writelines("\n".join(["가", "나", "다", "라", "마"]))
    wfile.write("\n")