def say_hello_name(name):
    print("안녕하세요, ", name)

def say_hello_name_msg(name, msg):
    print("안녕하세요, ", name, "님", msg)

def getSum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum