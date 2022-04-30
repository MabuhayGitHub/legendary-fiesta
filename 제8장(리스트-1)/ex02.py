STUDENT = 5

scores = []
score_sum = 0.0
score_avg = 0.0
cnt_80 = 0

for i in range(5):
    score = int(input("성적을 입력하세요 : "))
    scores.append(score)
    score_sum += score
    if score >= 80:
        cnt_80 += 1
    print(score, score_sum)
score_avg = score_sum / len(scores)
print(score_avg)
print(cnt_80)