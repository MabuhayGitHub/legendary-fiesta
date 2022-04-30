def pushfunc(data, n):
    data.append(n)

def popfunc(data):
    if len(data) > 0:
        data.pop()
        return
    else:
        print("스택이 비어있습니다.")

def pushData(stack):
    for i in range(1, 5):
        pushfunc(stack, i)
        print(stack)

def popData(stack):
    for i in range(1, 5):
            popfunc(stack)
            print(stack)

if __name__ == "__main__":
    stack = []
    pushData(stack)
    popData(stack)