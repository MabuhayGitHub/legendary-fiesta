def list_test(my_list):
    print("함수 내 (매개 변수) my_list 주소: ", id(my_list))
    my_list = [1, 2, 3, 4]
    print("함수 내 (매개 변수) my_list 할당 후 주소: ", id(my_list))
    print("함수 내부에서의 my_list: ", my_list)
    return

my_list = [100, 200, 300, 400]
print("함수 호출 전 my_list 주소: ", id(my_list))
list_test(my_list)
print("함수 호출 후 my_list 주소: ", id(my_list))
print("함수 외부에서의 ny_list: ", my_list)