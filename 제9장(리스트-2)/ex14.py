scores = [
            [ 95,  94, 100],
            [ 21,  22,  23],
            [ 34,  35,  36],
            [ 47,  48,  49],
            [ 50,  51,  52],
         ]

kTotal = 0
eTotal = 0
mTotal = 0

totalSum = kTotal + eTotal + mTotal
avg = 0.0

print("+----------------------------------------------+")
print("| 번호 | 국 어 | 영 어 | 수 학 | 총 점 | 평 균 |")
print("+----------------------------------------------+")

for i in range(len(scores)):
    sum = 0
    average = 0.0

    kTotal += scores[i][0]
    eTotal += scores[i][1]
    mTotal += scores[i][2]

    print("%5d" % (i+1), end="\t")

    for j in range(len(scores[i])):
        sum += scores[i][j]
        print("%5d" % scores[i][j], end="\t")
    print("%5d" % sum, end="\t")
    
    totalSum += sum
    average = sum / len(scores[i])
    avg += average
    # print("%3.2f" % average, end="\n")
    print("{0:.2f}".format(average))

avg /= len(scores)

print("+----------------------------------------------+")
print("  총점\t%5d\t%5d\t%5d\t%5d\t%.2f" % (kTotal, eTotal, mTotal, totalSum, avg))
print("+----------------------------------------------+")