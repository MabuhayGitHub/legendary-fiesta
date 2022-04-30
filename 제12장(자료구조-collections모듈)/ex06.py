from collections import defaultdict

def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        # counter[letter] += 1
    return counter

def countLetters_setdefault(word):
    counter = {}
    for letter in word:
        counter.setdefault(letter, 1)
    return counter

def countLetters_defaultdict(word):
    counter = defaultdict(lambda : 0)
    for letter in word:
        counter[letter] += 2
    return counter


if __name__ == "__main__":
    dic = countLetters("가나다라마")
    print(dic.items())
    dic = countLetters_setdefault("가나다라마")
    print(dic.items())
    dic = countLetters_defaultdict("가나다라마")
    print(dic.items())