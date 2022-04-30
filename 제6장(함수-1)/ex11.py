import random

def makeRandom():
    num_str = "0123456789"
    passwd = ""
    for i in range(6):
        index = random.randrange(len(num_str))
        passwd += num_str[index]
    return passwd

for i in range(3):
    print(makeRandom())