# TEXT MINING
def file_read(text):
    f_name = open("D:\\_PYTHON\\_Inflearn\\제12장(자료구조-collections모듈)\\law.txt", mode="r", encoding="UTF8")
    for line in f_name:
        words = line.strip().split()
        for word in words:
            if len(word) >= 2:
                text.append(word)




if __name__ == "__main__":
    from collections import defaultdict
    from collections import OrderedDict
    text = []
    file_read(text)
    word_count = defaultdict(lambda : 0)

    for word in text:
        word_count[word] += 1
    for i, v in OrderedDict(sorted(word_count.items(), key=lambda t:t[1], reverse=True)).items():
        if v >= 2:
            print(i, v)

