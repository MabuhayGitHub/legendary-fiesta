def main():
    f_name = open(file="C:\\Python\\Inflearn\\python\\제9장(리스트-2)\\data.csv", mode="r", encoding="UTF8")
    # read()
    # readline()
    # readlines()
    for line in f_name.readlines():
        line = line.strip()
        # print(line)
        # print(type(line))

        words = line.split(",")
        for word in words:
            print("   ", word)
    f_name.close()

if __name__ == "__main__":
    main()