def cleaning(word):
    out_str = ""
    for ch in word:
        if ch.isalpha():
            out_str += ch
    return out_str.lower

if __name__ == "__main__":
    words = set()
    # fname = input("파일명: ")
    # print(fname)
    # file = open("D:\\_PYTHON\\_Inflearn\\제10장(자료구조-스택,큐,튜플,세트)\\words.txt", mode="r", encoding="UTF8")
    fname = input("파일명: ")
    file = open(fname, mode="r", encoding="UTF8")
    for line in file:
        linewords = line.split()
        for word in linewords:
            words.add(word)

print(words)
print(len(words))