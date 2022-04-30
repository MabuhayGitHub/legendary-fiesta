import regex

string = "안녕 John 난 지금 학교 가고 있어"
li1 = string.split()
print(type(li1))
# <class 'list'>
print(li1)
# ['안녕', 'John', '난', '지금', '학교', '가고', '있어']

string = "안녕,John,난,지금,학교,가고,있어"
li2 = string.split(",")
print(li2)
# ['안녕', 'John', '난', '지금', '학교', '가고', '있어']


string = "안녕/John,난|지금,학교,가고,있어"
li3 = regex.split("[/,|]", string)
print(li3)
# ['안녕', 'John', '난', '지금', '학교', '가고', '있어']

string = "abcd"
print(string.isalpha())
# True

string = "1234"
print(string.isalpha())
# False
print(string.isdigit())
# True
print(string.isdecimal())
# True

string = "1234abcd"
print(string.isalnum())
# True

string = "1.2"
print(string.isnumeric())
# False

string = "   "
print(string.isspace())
# True