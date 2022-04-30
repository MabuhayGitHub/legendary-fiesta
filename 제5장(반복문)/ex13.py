cnt = 0
sum = 0
score = 0

print("음수를 입력하면 종료됩니다.(예: -1)")

while score >=0:
    score = int(input(str(cnt+1)+ "번째 학생의 성적을 입력해 주세요 : "))
    if score >= 0:
        sum += score
        cnt += 1
        avg = sum / cnt
    print(cnt, sum, avg)