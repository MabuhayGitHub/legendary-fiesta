from os import stat


statements = "   안녕!            "
print("입력: " + statements)
print("좌쪽: " + statements.lstrip())
print("우쪽: " + statements.rstrip())
print("양쪽: " + statements.strip())


# 문자열 나누기
statements = "나는 열심히 파이썬 공부를 합니다"
print(statements.split())