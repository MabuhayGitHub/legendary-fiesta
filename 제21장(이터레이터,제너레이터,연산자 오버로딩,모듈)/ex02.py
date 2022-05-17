# StopIteration 예외

list1 = [10, 20, 30]

# iter() 내장함수 -> 이터레이터로 사용할 수 있도록 설정
list1_iter = iter(list1)
# list1 = list1.__iter__()

print(list1_iter.__next__())
print(list1_iter.__next__())
print(list1_iter.__next__())
print(list1_iter.__next__())    # StopIteration 발생