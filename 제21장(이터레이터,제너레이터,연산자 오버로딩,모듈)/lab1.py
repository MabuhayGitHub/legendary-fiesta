# 피보나치 수열 만들기

class FibIterator(object):
    def __init__(self, a=0, b=1, maxValue=50000000000):
        self.a = a
        self.b = b
        self.maxValue = maxValue
    def __iter__(self):
        return self
    def __next__(self):
        n = self.a + self.b
        if n > self.maxValue:
            raise StopIteration
        self.a = self.b
        self.b = n
        # print(self.a, self.b)
        return n

if __name__ == "__main__":
    for n in FibIterator():
        print(n, end=" ")