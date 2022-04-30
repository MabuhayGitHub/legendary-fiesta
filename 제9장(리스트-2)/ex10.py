# list1 = [4, 8, 9, -1, 10]

# list1.sort()
# print(list1)

# list1.sort(reverse=True)
# print(list1)

import time

def selectionSort(li):
    for i in range(len(li)):
        print(i, li)
        min_idx = i
        for j in range(i+1, len(li)):
            if li[min_idx] > li[j]:
                min_idx = j
        if i != min_idx:
            li[i], li[min_idx] = li[min_idx], li[i]

def bubbleSort(li):
    list_length = len(li)
    for i in range(list_length-1):
        for j in range(list_length-i-1):
            print(li)
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
            time.sleep(1)

if __name__ == "__main__":
    li = [4, 6, 1, 10, 7, -7, -100, 15, 30, 15]
    selectionSort(li)
    print(li)
    li = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    bubbleSort(li)
    print(li)