import time


def offer(data, n):
    data.append(n)


def poll(data):
    if len(data) > 0:
        data.pop(0)
    return


def insert_offer(data):
    for i in range(1, 11):
        offer(data, i)
        print(data)
        time.sleep(1)


def delete_poll(data):
    for i in range(1, 11):
        poll(queue)
        print(queue)
        time.sleep(1)


if __name__ == "__main__":
    queue = []
    insert_offer(queue)
    delete_poll(queue)
