# 메서드의 다형성

class SalesWorker(object):
    def __init__(self, name):
        self.__name = name
    def work(self):
        print(self.__name)

class DevWorker(SalesWorker):
    def __init__(self, name):
        super().__init__(name)
        self.__name = name
    def work(self):
        print(self.__name)

if __name__ == "__main__":
    worker1 = SalesWorker("데이브")
    worker2 = SalesWorker("신은혁")
    worker3 = SalesWorker("김연아")
    worker4 = DevWorker("김갑수")
    worker5 = DevWorker("홍길동")
    worker6 = DevWorker("고길동")
    workers = [worker1, worker2, worker3, worker4, worker5, worker6]

    for worker in workers:
        worker.work()

