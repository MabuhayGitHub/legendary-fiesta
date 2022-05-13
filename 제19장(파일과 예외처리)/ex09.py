import csv

path = "C:/Python/Inflearn/python/제19장(파일과 예외처리)/files/"
filename = path + "weather.csv"

f = open(filename, "r")
data = csv.reader(f)

header = next(data)
# print(header)
temp = 1000
for row in data:
    if temp > float(row[3]):
        temp = float(row[3])
print("최저 기온: ", temp)

f.close()