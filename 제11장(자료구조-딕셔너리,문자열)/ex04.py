from turtle import end_fill


#f_name = input("파일 이름 입력: ")

# file = open(file=f_name, mode="r", encoding="UTF8")

file = open("C:\\Python\\Inflearn\\python\\제11장(자료구조-[딕셔너리,문자열,collections모듈)\\words.txt", mode="r", encoding="UTF8")
word_count = dict()
for line in file:
    words = line.split()
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
file.close()
print(word_count)