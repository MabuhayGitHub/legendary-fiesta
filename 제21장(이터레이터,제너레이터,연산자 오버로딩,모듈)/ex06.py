class NumBox(object):
    def __init__(self, num):
        self.num = num
    def __add__(self, num):
        self.num += num
    def __radd__(self, num):
        self.num += num
    def __sub__(self, num):
        self.num -= num
    def __rsub__(self, num):
        self.num -= num

# 개념 파악용, 실제 사용시 수정 필요
n = NumBox(40)
n + 100     # n.__add__(100)
print(n.num)
n - 110     # n.__sub__(110)
print(n.num)
100 + n
print(n.num)
200 - n
print(n.num)
