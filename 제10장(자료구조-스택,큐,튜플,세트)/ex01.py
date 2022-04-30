import time

# ##############################################################

# stack_data = []
# for i in range(10, 100, 10):
#     stack_data.append(i)
#     print(stack_data)
#     time.sleep(1)
# for _ in range(10, 100, 10):
#     stack_data.pop()
#     print(stack_data)
#     time.sleep(1)

# ##############################################################

words = input("문자열을 입력하세요: ")

words_list = list(words)
print(words_list)

result = []
for _ in range(len(words_list)):
    result.append(words_list.pop())
print(result)

# ##############################################################

