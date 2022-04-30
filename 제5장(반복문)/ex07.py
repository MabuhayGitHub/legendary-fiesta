# C = (F - 32) * 5 / 9
for t in range(0, 101, 10): 
    valC = (t - 32.0) * 5.0 / 9.0
    print(t, "->", round(valC,2))
