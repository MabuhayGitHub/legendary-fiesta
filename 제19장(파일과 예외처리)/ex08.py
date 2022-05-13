import csv

path = "C:/Python/Inflearn/python/제19장(파일과 예외처리)/files/"
filename = path + "weather.csv"

f = open(filename, "r")
data = csv.reader(f)

header = next(data)
print(header)
for row in data:
    pass
    # print(row)

f.close()