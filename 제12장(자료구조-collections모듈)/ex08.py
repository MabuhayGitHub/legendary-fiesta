from collections import defaultdict

def counterWords(words):
    grouper = defaultdict(set)
    for word in words:
        length = len(word)
        grouper[length].add(word)
    return grouper

if __name__ == "__main__":
    set1 = set()
    set1.add("한국")
    set1.add("미국")
    set1.add("우즈베키스탄")
    set1.add("스페인")
    set1.add("스위스")
    set1.add("영국")
    set1.add("사우디아라비아")
    dic1 = counterWords(set1)
    print(dic1)
