# def test():
#     # print(text)
#     text = "Python"
#     print(text)

# text = "Java"
# test()
# print(text)

def test():
    global text
    print(text)
    text = "Python"
    print(text)

text = "Java"
print(text)
test()
print(text)